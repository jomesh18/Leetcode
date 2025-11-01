# semi_auto_login_playwright.py
import json
import time
import requests
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://www.lotteryagent.kerala.gov.in/usr/nicsl/login"
LOGGED_IN_URL = "https://www.lotteryagent.kerala.gov.in/dashboard"
PRIZE_URL = "https://www.lotteryagent.kerala.gov.in/agent/4545sd/payment"

OFFICE_SELECT_ID = "office"
PRIZE_TYPE_SELECT_ID = "prizeType"
SELECT_ALL_SELECTOR = 'input[onclick*="selectall"]'
CHECKBOX_SELECTOR = 'input[name="select[]"]'
GENERATE_VOUCHER_BUTTON = "#generate_button" 
OTP_INPUT_SELECTOR = '#kurachu_samayathe_thakol'
# NAME = "E9826"
# LOGIN = "jomonKR@123"
NAME = "E11390"
LOGIN = "Sahayee123@"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto(LOGIN_URL)
    # Fill credentials (update selectors as necessary)
    page.fill('input[name="_peru"]', NAME)
    page.fill('input[name="_thakol"]', LOGIN)

    print("Please solve CAPTCHA in the browser window and log in.")

    page.wait_for_url(LOGGED_IN_URL, timeout=300000)  # 300s
    print("Logged in")
    
    # --- NAVIGATE TO PRIZE REQUEST PAGE ---
    page.goto(PRIZE_URL)
    page.wait_for_load_state("networkidle")
    print("✅ Opened Agent Prize Request page")


    # --- SELECT FIELDS ---
    page.select_option(f"select#{OFFICE_SELECT_ID}", value="8")  # example office ID
    page.select_option(f"select#{PRIZE_TYPE_SELECT_ID}", value="1")  # example prize type ID
    print("Selected Office and Prize Type")

    # --- WAIT FOR CHECKBOXES TO LOAD ---
    page.wait_for_selector(CHECKBOX_SELECTOR, timeout=20000)
    print("Prize list loaded.")

    # Click using JS, passing the selector variable into page.evaluate
    page.evaluate(
        """(selector) => {
            const el = document.querySelector(selector);
            if (el) el.click();
            else console.error('Select All checkbox not found!');
        }""",
        SELECT_ALL_SELECTOR
    )

    print('Clicked the select all checkbox')
    # Wait briefly for all selections to update (since getTotal() might take a moment)
    page.wait_for_timeout(1000)
    # Locate all prize checkboxes
    checkboxes = page.locator('input[name="select[]"]')
    # Count how many are checked
    checked_count = checkboxes.evaluate_all(
        "(boxes) => boxes.filter(b => b.checked).length"
    )
    total_count = checkboxes.count()
    print(f"Checked: {checked_count} / Total: {total_count}")
    if not (checked_count == total_count):
        print("⚠️ Not all checkboxes are selected! Skipping OTP submission.")
        browser.close()

    print("✅ All checkboxes selected. Proceeding to Generate OTP...")
    page.screenshot(path="checkboxes_selected.png")

    # --- SUBMIT FORM ---
    page.click(GENERATE_VOUCHER_BUTTON)
    print("Submitted to generate otp")
    


    print("📩 Looking for visible OTP field among duplicates...")

    page.wait_for_function(
        """() => {
            const els = document.querySelectorAll('#kurachu_samayathe_thakol');
            for (const el of els) {
                const rect = el.getBoundingClientRect();
                const visible =
                    el.offsetParent !== null &&
                    rect.width > 0 && rect.height > 0 &&
                    window.getComputedStyle(el).visibility !== 'hidden' &&
                    window.getComputedStyle(el).display !== 'none';
                if (visible) {
                    window.__otpField = el; // store the visible one globally
                    return true;
                }
            }
            return false;
        }""",
        timeout=300000
    )



    print("🔢 OTP field detected! Please enter the OTP manually in the browser.")

    # Wait until OTP field has *enough digits* (e.g., 6 digits)
    page.wait_for_function(
        """() => window.__otpField && window.__otpField.value.trim().length >= 6""",
        timeout=300000
    )
    print("✅ OTP entered, proceeding to click VERIFY button...")

    # Wait for a visible Verify button before clicking
    page.wait_for_function(
        """() => {
            const els = document.querySelectorAll('#verifyotp');
            for (const el of els) {
                const rect = el.getBoundingClientRect();
                const visible =
                    el.offsetParent !== null &&
                    rect.width > 0 && rect.height > 0 &&
                    window.getComputedStyle(el).visibility !== 'hidden' &&
                    window.getComputedStyle(el).display !== 'none';
                if (visible) {
                    window.__verifyButton = el;
                    return true;
                }
            }
            return false;
        }""",
        timeout=60000
    )

    # Click the visible Verify OTP button after OTP is entered
    page.evaluate("""
        window.__verifyButton.scrollIntoView({behavior: 'smooth', block: 'center'});
        window.__verifyButton.click();
    """)

    print("🟢 VERIFY OTP button clicked — waiting for response...")

    # Wait for the network response to voucherVerifyOtp
    with page.expect_response(lambda r: 'voucherVerifyOtp' in r.url and r.request.method == 'POST') as otp_response_info:
        pass  # this pauses until the network call returns

    otp_response = otp_response_info.value
    print(f"🔍 OTP verify response status: {otp_response.status}")

    # Try to decode the response body if it’s JSON or text
    try:
        otp_data = otp_response.json()
    except Exception:
        otp_data = otp_response.text()

    print(f"📦 OTP verification response:\n{otp_data}")

    # Check success/failure
    if isinstance(otp_data, dict) and ('success' in otp_data or 'verified' in str(otp_data).lower()):
        print("🎉 OTP verified successfully! Continuing...")
    else:
        print("❌ OTP verification failed or invalid. Please check the OTP and try again.")

    time.sleep(100)

    browser.close()
