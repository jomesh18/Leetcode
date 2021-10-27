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

from tkinter import *
from tkinter import ttk

class FindAccBox:

    def __init__(self, root):
        root.title("Sahayee Acc")
        root.geometry("500x200")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe = ttk.Frame(root, padding="3 3 12 12", width = 500, height = 200)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.item = StringVar()
        item_entry = ttk.Entry(mainframe, width=7, textvariable=self.item)
        item_entry.grid(column=3, row=1, sticky=(W, E))

        self.box = StringVar()
        ttk.Label(mainframe, textvariable=self.box).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="Search", command=self.get_box).grid(column=3, row=3, sticky=W)

        # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is in box").grid(column=1, row=2, sticky=E)
        # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        item_entry.focus()
        root.bind("<Return>", self.get_box)


    def get_box(self, *args):
        key = self.item.get().lower()
        if key in d:
            return self.box.set(d[key])

    def add_to_dictionary(self):
        key, box = input()
        d[key] = box

    def delete_from_dictionary(self):
        key = input()
        if key in d:
            del d[key]

root = Tk()
FindAccBox(root)
root.mainloop()
