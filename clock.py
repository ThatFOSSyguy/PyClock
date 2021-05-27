# Importing
from tkinter import *
from tkinter.ttk import *
from time import strftime

tk = Tk()
tk.title('PyClock') # Tittle

# Calculating the time
def clockTime():
	string = strftime('%H:%M:%S %p')
	label.config(text=string)
	label.after(1000, clockTime) # Looping the functions after 1000 seconds

# Giving the clock drip
label = Label(tk, font=("Segoe UI", 80), background="black", foreground="cyan")
label.pack(anchor='center')
clockTime()

mainloop()
