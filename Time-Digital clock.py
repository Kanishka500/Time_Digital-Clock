from tkinter import*
import time

window = Tk()
window.title("My First GUI Form")

time_format = time.strftime("%I:%M:%S %p")


lbl1 = Label(window,text=time_format,font=("Calibri",30))
lbl1.pack()

window.mainloop()
