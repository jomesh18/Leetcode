from tkinter import *
from tkinter import ttk
root = Tk()
frame =ttk.Frame(root)
frame['width'] = 1000
frame['height'] = 500
frame.grid()
frame['padding'] = 5
frame['borderwidth'] = 5
frame['relief'] = 'ridge'
b1 = ttk.Button(frame, text='click1').grid()
b2 = ttk.Button(frame, text='click2').grid()

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(frame, width=200, height=200, style='Danger.TFrame').grid()

root.mainloop()