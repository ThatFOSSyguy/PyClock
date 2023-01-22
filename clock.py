from tkinter import *
from time import *

def updateEverything():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    clockWindow.after(1000,updateEverything)


clockWindow = Tk()
clockWindow.title('PyClock')

time_label = Label(clockWindow,font=("Segoe UI",50),fg="#00FFFF",bg="black")
time_label.pack()

day_label = Label(clockWindow,font=("Segoe UI",25,"bold"))
day_label.pack()

updateEverything()
clockWindow.mainloop()
