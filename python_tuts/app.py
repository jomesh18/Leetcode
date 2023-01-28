# 1
#db


# import sqlite3

# connect = sqlite3.connect('data.db')

# connect.execute("DROP TABLE IF EXISTS CUSTOMER")
# connect.execute('''CREATE TABLE CUSTOMER 
#                 (ID INT PRIMARY KEY NOT NULL,
#                 NAME TEXT NOT NULL,
#                 AGE INTEGER NOT NULL);''')
# connect.execute("INSERT INTO CUSTOMER  (ID, NAME, AGE) \
#     VALUES (1, 'XYZ', 29)")
# connect.execute("INSERT INTO CUSTOMER  (ID, NAME, AGE) \
#     VALUES (2, 'abc', 19)")
# all_data = connect.execute('''SELECT * FROM CUSTOMER''')
# for row in all_data:
#     print(row)

# connect.close()



# 2
# using apis in python
# how to use apis


# import requests
# import json

# response = requests.get("https://api.tomitokko.repl.co/")

# print(response.status_code)

# # print(response.text)

# #prints every single character because it sees this as a single thing, so we use json
# # for res in response.text:
# #     print(res)

# res = json.loads(response.text)

# # print(res)
# for data in res:
#     print(data)



#3
# classes
# too basic, i know this


#web scraping with python
'''
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.codewithtomi.com/")

# print(res.text) # gets all html code from the page
# print(res)

soup = BeautifulSoup(res.content, "html.parser")
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)
# print(soup.title.parent)

# s = soup.find('h2', class_='post-title') #find the content with h2 tag with class post-title
# print(s)

# s = soup.find_all('h2', class_='post-title') #find the content with h2 tag with class post-title
# print(s)

# s = soup.find('h2', class_='post-title') #find the content with h2 tag with class post-title
# print(s.text)

# s = soup.find_all('h2', class_='post-title') #find the content with h2 tag with class post-title
# for data in s:
#     print(data.text)


s = soup.find_all('p', class_='post-snippet') #find the content with h2 tag with class post-title
for data in s:
    print(data.text)

'''


# 4. Virtual environments
# pretty basic


'''
# flask setup
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h2>Welcome to my web app</h2>'

# in terminal run 'python -m flask run'
'''


#django setup
