from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont



def read_file():
    d = {}
    with open('acc.txt', 'r', encoding='utf-8') as file:
        for line in file:
            model_string, box = line.strip().split(':')
            box = box.strip()
            for model in model_string.strip().split(','):
                model = model.strip()
                if model not in d:
                    d[model] = set()
                d[model].add(box)
    for key in d:
        d[key] = ', '.join(d[key])
    return d

class FindAccBox:
    def __init__(self, root):
        root.title('Acc App')
        self.largefontStyle = tkFont.Font(family="Lucida Grande", size=50)
        self.smallfontStyle = tkFont.Font(family="Lucida Grande", size=25)
        width= root.winfo_screenwidth()-50 
        height= root.winfo_screenheight()-50
        #setting tkinter window size
        root.geometry('%dx%d+%d+%d' % (width, height, 0, 0))

        self.entry_var = StringVar()
        self.entry_var.trace_add("write", self.update_list)
        self.model_var = StringVar()
        self.box_var =  StringVar()

        frame = ttk.Frame(root)
        ttk.Label(frame, text='Search model', font=self.largefontStyle).grid(row=1, column=0, padx=5)
        self.entry = ttk.Entry(frame, font=self.smallfontStyle, textvariable=self.entry_var)
        self.s = ttk.Scrollbar(frame, orient='vertical', command=self.listbox_scroll)
        self.model_list = Listbox(frame, listvariable=self.model_var, yscrollcommand=self.yscroll1, selectmode=SINGLE, font=self.smallfontStyle)
        self.box_list = Listbox(frame, listvariable=self.box_var, yscrollcommand=self.yscroll2, selectmode=SINGLE, font=self.smallfontStyle)


        frame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
        self.entry.grid(row=1, column=1, sticky=NSEW)
        self.model_list.grid(row=2, column=0, sticky=NSEW)
        self.box_list.grid(row=2, column=1, sticky=NSEW)
        self.s.grid(row=2, column=3)

        for i in range(3):
            for j in range(3):
                frame.config(padding=5)

        root.columnconfigure(0, weight=2)
        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=2)
        root.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=5)

        self.entry.focus()
        
    def yscroll1(self, *args):
        if self.box_list.yview() != self.model_list.yview():
            self.box_list.yview_moveto(args[0])
        self.s.set(*args)

    def yscroll2(self, *args):
        if self.box_list.yview() != self.model_list.yview():
            self.model_list.yview_moveto(args[0])
        self.s.set(*args)

    def listbox_scroll(self, *args):
        self.model_list.yview(*args)
        self.box_list.yview(*args)

    def update_list(self, *args):
        search_term =  ''.join(self.entry_var.get().strip().split(' ')).upper()
        self.box_list.delete(0, END)
        self.model_list.delete(0, END)
        for key, value in d.items():
            curr_key = ''.join(key.strip().split(' ')).upper()
            if search_term in curr_key:
                self.box_list.insert(END, value)
                self.model_list.insert(END, key)

root = Tk()

obj = FindAccBox(root)

d = read_file()
obj.update_list()
root.mainloop()
