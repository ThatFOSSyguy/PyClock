from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('PyClock')

def clockTime():
	string = strftime('%H:%M:%S %p')
	label.config(text=string)
	label.after(1000, clockTime)

label = Label(root, font=("Segoe UI", 80), background="black", foreground="cyan")
label.pack(anchor='center')
clockTime()

mainloop()