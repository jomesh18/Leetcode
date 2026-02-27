from tkinter import *
import tkinter.font as tkFont



def read_file():
    d = {}
    with open('acc.txt', 'r', encoding='utf-8') as file:
        for line in file:
            model_string, box = line.strip().split(':')
            box = box.strip()
            model_string = model_string.strip()
            d[model_string] = box
    return d

class FindAccBox:
    def __init__(self, root):
        root.title('Acc App')
        # root['bg'] = 'Red'
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


        frame1 = Frame(root)
        frame2 = Frame(root)
        label = Label(frame1, text='Search model', font=self.largefontStyle)
        self.entry = Entry(frame1, font=self.smallfontStyle, textvariable=self.entry_var)
        self.model_list = Listbox(frame2, listvariable=self.model_var, yscrollcommand=self.yscroll1, selectmode=SINGLE, font=self.smallfontStyle)
        self.box_list = Listbox(frame2, listvariable=self.box_var, yscrollcommand=self.yscroll2, selectmode=SINGLE, font=self.smallfontStyle, width=10)
        self.s = Scrollbar(frame2, orient='vertical', command=self.listbox_scroll)

        frame1.grid(row=0, column=0, sticky=EW)
        frame2.grid(row=1, column=0, sticky=NSEW)
        label.grid(row=0, column=0, padx=5)
        self.entry.grid(row=0, column=1, sticky=NSEW)
        self.model_list.grid(row=0, column=0, sticky=NSEW)
        self.box_list.grid(row=0, column=1, sticky=NS)
        self.s.grid(row=0, column=2, sticky=NS)

        for child in frame1.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in frame2.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=10)
        frame1.columnconfigure(0, weight=1)
        frame1.columnconfigure(1, weight=5)
        
        frame2.rowconfigure(0, weight=10)
        frame2.columnconfigure(0, weight=10)


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
        i = 0
        for key, value in d.items():
            curr_key = ''.join(key.strip().split(' ')).upper()
            if search_term in curr_key:
                self.box_list.insert(END, value)
                self.model_list.insert(END, key)
                if i & 1:
                    self.box_list.itemconfigure(i, background="#f0f0ff")
                    self.model_list.itemconfigure(i, background='#f0f0ff')
                i += 1

root = Tk()

obj = FindAccBox(root)

d = read_file()
obj.update_list()
root.mainloop()
