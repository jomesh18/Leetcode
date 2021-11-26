from tkinter import *
import tkinter.font as tkFont

class FindAccBox:

    def __init__(self, root):
        self.largefontStyle = tkFont.Font(family="Lucida Grande", size=50)
        self.smallfontStyle = tkFont.Font(family="Lucida Grande", size=25)
        root.title("Sahayee Acc")
        width= root.winfo_screenwidth()-20 
        height= root.winfo_screenheight()-100
        #setting tkinter window size
        root.geometry('%dx%d+%d+%d' % (width, height, 0, 0))
        # root.geometry("600x200")

        Grid.columnconfigure(root, 0, weight=1)
        Grid.rowconfigure(root, 0, weight=1)

        mainframe = Frame(root)
        mainframe.grid(row=0, column=0, sticky="NSEW")

        for i in range(1):
            Grid.rowconfigure(mainframe, i, weight=1)
            for j in range(2):
                Grid.columnconfigure(mainframe, j, weight=1)

        i = 3
        Grid.rowconfigure(mainframe, i, weight=1)
        for j in range(2):
            Grid.columnconfigure(mainframe, j, weight=1)

        i = 2
        Grid.rowconfigure(mainframe, i, weight=1)
        for j in range(3):
            Grid.columnconfigure(mainframe, j, weight=1)

        # print(mainframe.grid_size())
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.box = StringVar()
        self.model_var = StringVar()

        #the shared scrollbar
        self.scrollbar = Scrollbar(mainframe, orient='vertical')

        Label(mainframe, text="ENTER MODEL", font=self.largefontStyle).grid(row=0, column=0, sticky='NSEW')
        self.item_entry = Entry(mainframe, font=self.smallfontStyle, textvariable=self.search_var)
        # item_entry.insert(0, "Enter the model name")
        self.item_entry.grid(row=1, column=0, sticky='NSEW')
        self.lbox_models = Listbox(mainframe, font=self.smallfontStyle,listvariable=self.model_var, selectmode=SINGLE, yscrollcommand=self.yscroll1)
        self.lbox_models.grid(row=1, column=1, sticky='NSEW')
        # self.lbox_models.bind('<<ListboxSelect>>', self.item_selected)
        self.lbox_box = Listbox(mainframe, font=self.smallfontStyle, selectmode=SINGLE, yscrollcommand=self.yscroll2)
        self.lbox_box.grid(row=1, column=2, sticky='NSEW')

        self.scrollbar.config(command=self.yview)
        self.scrollbar.grid(row=1, column=3)

        Button(mainframe, text="ADD MODEL", font=self.smallfontStyle, command=self.add_button_window).grid(row=2, column=0, pady=10, sticky='NSEW')        
        Button(mainframe, text="REMOVE MODEL", font=self.smallfontStyle, command=self.delete_button_window).grid(row=2, column=1, pady=10, sticky='NSEW')

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.item_entry.focus()
    
    def yscroll1(self, *args):
        if self.lbox_box.yview() != self.lbox_models.yview():
            self.lbox_box.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll2(self, *args):
        if self.lbox_models.yview() != self.lbox_box.yview():
            self.lbox_models.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yview(self, *args):
        self.lbox_models.yview(*args)
        self.lbox_box.yview(*args)

    def update_list(self, *args):
        search_term = self.search_var.get()
        try:
            self.message_label.config(text="")
        except:
            pass
        # Just a generic list to populate the listbox
        lbox_list = [(key, val) for key, val in d.items()]
        # print(lbox_list)

        self.lbox_models.delete(0, END)
        self.lbox_box.delete(0, END)

        for item in lbox_list:
            if search_term.upper() in item[0]:
                self.lbox_models.insert(END, item[0])
                self.lbox_box.insert(END, str(item[1]))

    def add_button_window(self):
        new = Toplevel(root)
        new.title("ADD MODELS")
        width= root.winfo_screenwidth()-20
        height= root.winfo_screenheight()-100
        #setting tkinter window size
        new.geometry('%dx%d+%d+%d' % (width, height, 0, 0))
        Grid.columnconfigure(new, 0, weight=1)
        Grid.rowconfigure(new, 0, weight=1)
        mainframe1 = Frame(new)
        mainframe1.grid(row=0, column=0, sticky='NSEW')

        Label(mainframe1, text="ENTER MODEL", font=self.smallfontStyle).grid(row=0, column=0, sticky='nsew')
        Label(mainframe1, text="ENTER BOX", font=self.smallfontStyle).grid(row=0, column=1, sticky='nsew')
        model_entry = Entry(mainframe1, textvariable=self.search_var, font=self.smallfontStyle)
        model_entry.grid(row=1, column=0, sticky='nsew')
        key_entry = Entry(mainframe1, textvariable=self.box, font=self.smallfontStyle)
        key_entry.grid(row=1, column=1, sticky='nsew')
        Button(mainframe1, text="ADD", font=self.smallfontStyle, command=self.add_to_dictionary).grid(row=2, column=0, sticky='nsew')
        Button(mainframe1, text="CLOSE", font=self.smallfontStyle, command=new.destroy).grid(row=2, column=1, sticky='nsew')

        self.message_label = Label(mainframe1, font=self.smallfontStyle)
        self.message_label.grid(row=3, column=0, sticky='NSEW')

        for row in range(3):
            Grid.rowconfigure(mainframe1, row, weight=1)
            for col in range(2):
                Grid.columnconfigure(mainframe1, col, weight=1)

        model_entry.focus()

    def delete_button_window(self):
        new = Toplevel(root)
        new.title("REMOVE MODELS")
        width= root.winfo_screenwidth()-20
        height= root.winfo_screenheight()-100
        #setting tkinter window size
        new.geometry('%dx%d+%d+%d' % (width, height, 0, 0))
        Grid.columnconfigure(new, 0, weight=1)
        Grid.rowconfigure(new, 0, weight=1)

        mainframe1 = Frame(new)
        mainframe1.grid(row=0, column=0, sticky='NSEW')

        Label(mainframe1, text="ENTER MODEL NUMBER", font=self.smallfontStyle).grid(row=0, column=0, sticky='nsew')
        model_entry = Entry(mainframe1, font=self.smallfontStyle, textvariable=self.search_var)
        model_entry.grid(row=1, column=0, sticky='nsew')
        
        self.lbox_models1 = Listbox(mainframe1, font=self.smallfontStyle,listvariable=self.model_var, selectmode=SINGLE)
        self.lbox_models1.grid(row=1, column=1, sticky='NSEW')

        Button(mainframe1, text="REMOVE",font=self.smallfontStyle, command=self.delete_from_dictionary).grid(row=2, column=0, sticky='nsew')
        Button(mainframe1, text="CLOSE", font=self.smallfontStyle, command=new.destroy).grid(row=2, column=1, sticky='nsew')

        self.message_label = Label(mainframe1, font=self.smallfontStyle)
        self.message_label.grid(row=3, column=0, sticky='NSEW')

        for row in range(3):
            Grid.rowconfigure(mainframe1, row, weight=1)
            for col in range(2):
                Grid.columnconfigure(mainframe1, col, weight=1)

        model_entry.focus()

    def add_to_dictionary(self, *args):
        key, box = self.search_var.get().upper(), self.box.get()
        if key not in d:
            d[key] = box
            with open('acc.txt', 'a+') as acc_file:
                acc_file.write('{}: {}\n'.format(key, box))
        self.message_label.config(text="Added successfully")

    def delete_from_dictionary(self, *args):
        key = self.search_var.get().upper()
        if key in d:
            del d[key]
        self.message_label.config(text="Removed successfully")

root = Tk()
# invoke the button on the return key
root.bind_class("Button", "<Key-Return>", lambda event: event.widget.invoke())

# remove the default behavior of invoking the button with the space key
root.unbind_class("Button", "<Key-space>")

obj = FindAccBox(root)
# app=FullScreenApp(root)

d = {}

with open('acc.txt', 'r') as acc_file:
    for line in acc_file: 
        key, val = line.split(':')
        d[key] = val
obj.update_list()
root.mainloop()
