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

root = Tk()
root.title('Acc App')
frame = ttk.Frame(root)
label = ttk.Label(frame, text='Search model')
entry = ttk.Entry(frame)
text = Text(frame)

frame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
label.grid(row=1, column=0, padx=5)
entry.grid(row=1, column=1, sticky=NSEW)
text.grid(row=2, column=0, columnspan=2, sticky=NSEW)

root.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=5)



root.mainloop()

