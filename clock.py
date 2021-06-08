""" 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
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
clockWindow.title('PyClock')# Tittle

time_label = Label(clockWindow,font=("Segoe UI",50),fg="#00FFFF",bg="black")
time_label.pack()# The time of the clock

day_label = Label(clockWindow,font=("Segoe UI",25,"bold"))
day_label.pack()# Day

updateEverything()
clockWindow.mainloop()
