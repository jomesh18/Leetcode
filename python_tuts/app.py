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
# oops
