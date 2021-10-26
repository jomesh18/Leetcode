import pyinputplus as pyip
d = {'a21s': 1, 
    'a71': 1, 
    'poco x3': 1, 
    'poco x2': 1, 
    'redmi note 9': 1, 
    'redmi note 10 pro max': 1,
    'samsung m51': 1,
    'samsung a51': 2,
    'redmi note 10': 2,
    'realme 5': 3, 
    'realme c11': 3, 
    'realme c21': 3, 
    'realme c15': 3, 
    'realme y20': 3, 
    'realme y20g': 3,
    'vivo iq': 3,
    'oppo a5 2020': 3, 
    'oppo a9 2020': 3
    }

inp = input().lower()
print(d.get(inp))