import sqlite3

# Connect to database (creates it if it doesn't exist)
connection = sqlite3.connect('acc.db')
cursor = connection.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS acc_box (
        name TEXT NOT NULL,
        box TEXT(20) NOT NULL
    )
''')

# Commit and close
connection.commit()
connection.close()

print("Table 'acc_box' created successfully.")


def initial_read():
    l = []
    with open('acc.txt', 'r', encoding='utf-8') as file:
        for line in file:
            model_string, box = line.strip().split(':')
            box = box.strip()
            model_string = model_string.strip()
            l.append((model_string, box))
    # print(l)
    # print(len(l))
    return l

def insert_multiple_accounts():
    """
    account_list should be a list of tuples: [('Name', 'BoxID'), ...]
    # # --- Example Usage ---
    # data_to_add = [
    #     ("Alice Smith", "BOX-101"),
    #     ("Bob Jones", "BOX-102"),
    #     ("Charlie Brown", "BOX-103"),
    #     ("Diana Prince", "BOX-104")
    # ]

    # insert_multiple_accounts(data_to_add)
    """
    try:
        account_list = initial_read()

        conn = sqlite3.connect('acc.db')
        cursor = conn.cursor()

        # The 'executemany' method is built for bulk operations
        cursor.executemany("INSERT INTO acc_box (name, box) VALUES (?, ?)", account_list)

        # One single commit for the entire batch
        conn.commit()
        print(f"Successfully inserted {cursor.rowcount} records.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        # Rollback if something goes wrong to keep data clean
        if conn:
            conn.rollback()
            
    finally:
        if conn:
            conn.close()

# insert_multiple_accounts()

def insert_account(name, box_id):
    # Example usage:
    # insert_account("John Doe", "BOX-001")
    try:
        # Connect to the database
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()

        # Use parameterized queries to prevent SQL injection
        sql = "INSERT INTO acc_box (name, box) VALUES (?, ?)"
        cursor.execute(sql, (name, box_id))

        conn.commit()
        print(f"Successfully added: {name}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        
    finally:
        if conn:
            conn.close()


def get_all_to_dict():
    # --- Example Usage ---
    # all_records = get_all_to_dict()

    # print(f"Total records found: {len(all_records)}")
    # print(all_records)
    try:
        conn = sqlite3.connect('acc.db')
        cursor = conn.cursor()

        # Select all columns from the table
        cursor.execute("SELECT name, box FROM acc_box")
        rows = cursor.fetchall()

        # Convert list of tuples [(name1, box1), (name2, box2)] into a dictionary
        # {name1: box1, name2: box2}
        acc_dict = {name: box for name, box in rows}
        
        return acc_dict

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {}
    finally:
        if conn:
            conn.close()

d = get_all_to_dict()
print(len(d))
