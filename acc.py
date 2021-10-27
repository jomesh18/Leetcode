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
import shelve

shelffile = shelve.open('acc_box')
# shelffile['d'] = d
d = shelffile['d']
print(d)
# shelffile.close()

class FindAccBox:

    def __init__(self, root):
        root.title("Sahayee Acc")
        root.geometry("500x200")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe = ttk.Frame(root, padding="3 3 12 12", width = 500, height = 200)
        # mainframe.grid(row=0, column=0, sticky=(N, W, E, S))

        self.item = StringVar()
        self.box = StringVar()

        ttk.Label(mainframe, text="Enter model number").grid(row=0, column=0, columnspan=2, sticky='ew')
        item_entry = ttk.Entry(mainframe, width=7, textvariable=self.item)
        item_entry.grid(row=0, column=2, sticky='ew', columnspan=2)
        ttk.Button(mainframe, text="Search", command=self.get_box).grid(row=0, column=4, sticky='ew')
        ttk.Label(mainframe, text="Box").grid(row=1, column=0, columnspan=2, sticky=E)
        ttk.Label(mainframe, textvariable=self.box).grid(row=1, column=2, sticky=(W, E))

        ttk.Button(mainframe, text="Add model", command=self.add_button_window).grid(row=3, column=0, sticky='ew')        
        ttk.Button(mainframe, text="Delete model", command=self.delete_button_window).grid(row=3, column=2, sticky='ew')

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        item_entry.focus()
        root.bind("<Return>", self.get_box)
        mainframe.pack(expand=True)

    def add_button_window(self):
        new = Toplevel(root)
        new.title("Add models")
        new.geometry("500x200")
        new.columnconfigure(0, weight=1)
        new.rowconfigure(0, weight=1)
        mainframe1 = ttk.Frame(new, padding="3 3 12 12", width = 500, height = 200)

        ttk.Label(mainframe1, text="Enter model number").grid(row=0, column=0, columnspan=2, sticky='ew')
        model_entry = ttk.Entry(mainframe1, width=10, textvariable=self.item)
        model_entry.grid(row=1, column=0, sticky='ew', columnspan=2)
        key_entry = ttk.Entry(mainframe1, width=10, textvariable=self.box)
        key_entry.grid(row=1, column=2, sticky='ew', columnspan=1)

        ttk.Button(mainframe1, text="Add", command=self.add_to_dictionary).grid(row=2, column=0, sticky='ew')
        mainframe1.pack(expand=True)

    def delete_button_window(self):
        new = Toplevel(root)
        new.title("Delete models")
        new.geometry("500x200")
        new.columnconfigure(0, weight=1)
        new.rowconfigure(0, weight=1)
        mainframe1 = ttk.Frame(new, padding="3 3 12 12", width = 500, height = 200)

        ttk.Label(mainframe1, text="Enter model number").grid(row=0, column=0, columnspan=2, sticky='ew')
        model_entry = ttk.Entry(mainframe1, width=10, textvariable=self.item)
        model_entry.grid(row=1, column=0, sticky='ew', columnspan=2)

        ttk.Button(mainframe1, text="Delete", command=self.add_to_dictionary).grid(row=2, column=0, sticky='ew')
        mainframe1.pack(expand=True)

    def get_box(self, *args):
        key = self.item.get().lower()
        if key in d:
            return self.box.set(d[key])

    def add_to_dictionary(self, *args):
        key, box = self.item.get().lower(), self.box.get()
        print(key, box)
        d[key] = box
        shelffile['d'] = d
        shelffile.close()
        shelffile = shelve.open('acc_box')
        d = shelffile['d']


    def delete_from_dictionary(self, *args):
        key = self.item.get().lower()
        if key in d:
            del d[key]
        shelffile['d'] = d
        shelffile.close()
        shelffile = shelve.open('acc_box')
        d = shelffile['d']

root = Tk()
FindAccBox(root)
root.mainloop()
