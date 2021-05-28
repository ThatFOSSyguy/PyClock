# Importing tkinter for UI and time for mesuring time
from tkinter import *
from time import *

# Updating the clock so that it goes for infinity
def updateEverything():
    time_string = strftime("%I:%M:%S %p")# Changed the %H to %I so it display 12hr clock
    time_label.config(text=time_string)

    day_string = strftime("%A")# The day counter
    day_label.config(text=day_string)

    clockWindow.after(1000,updateEverything)# Updating the window after 1000 seconds(1 hour).


clockWindow = Tk()
clockWindow.title('PyClock (Development branch)')# Tittle

time_label = Label(clockWindow,font=("Segoe UI",50),fg="#00FFFF",bg="black")
time_label.pack()# The time of the clock

day_label = Label(clockWindow,font=("Segoe UI",25,"bold"))
day_label.pack()# Day

updateEverything()
clockWindow.mainloop()
