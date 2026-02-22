from tkinter import *
from tkinter import ttk


def read_file():
    d = {}
    with open('acc.txt', 'r', encoding='utf-8') as file:
        for line in file:
            model_string, box = line.strip().split(':')
            box = box.strip()
            for model in model_string.strip().split(','):
                model = model.strip()
                if model not in d:
                    d[model] = []
                d[model].append(box)
    return d

def yscroll1(args):
    if box_list.yview() != model_list.yview():
        box_list.yview_moveto(args[0])
    s.set(*args)

def yscroll2(args):
    if box_list.yview() != model_list.yview():
        model_list.yview_moveto(args[0])
    s.set(*args)

def listbox_scroll(args):
    model_list.yview(*args)
    box_list.yview(*args)

def update_list(d, entry_var, l1_var, l2_var):
    if not entry_var:
        l1_var.set(d.keys())
        l2_var.set(d.values())
    else:
        models = []
        boxes = []
        for key in d:
            if entry_var in d:
                models.append(key)
                boxes.append(d[key])
        l1_var.set(models)
        l2_var.set(boxes)

root = Tk()
root.title('Acc App')

entry_var = StringVar()
entry_var.trace_add("write", update_list)
model_var = StringVar()
box_var =  StringVar()


frame = ttk.Frame(root)
label = ttk.Label(frame, text='Search model')
entry = ttk.Entry(frame, textvariable=entry_var)
s = ttk.Scrollbar(frame, orient='vertical', command=listbox_scroll)
model_list = Listbox(frame, listvariable=model_var, yscrollcommand=yscroll1)
box_list = Listbox(frame, listvariable=box_var, yscrollcommand=yscroll2)


frame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
label.grid(row=1, column=0, padx=5)
entry.grid(row=1, column=1, sticky=NSEW)
model_list.grid(row=2, column=0, sticky=NSEW)
box_list.grid(row=2, column=1, sticky=NSEW)
s.grid(row=2, column=3)

root.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=5)


entry.focus()
root.mainloop()

