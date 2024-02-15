from tkinter import *

parent=Tk()
parent.geometry("100x100")
redbutton=Button(parent,text="RED",bg='red',fg='white')
redbutton.pack(side="left")

redbutton=Button(parent,text="GREEN",bg='green',fg='white')
redbutton.pack(side="right")

redbutton=Button(parent,text="BLUE",bg='blue',fg='white')
redbutton.pack(side="top")

redbutton=Button(parent,text="Black",bg='black',fg='white')
redbutton.pack(side="bottom")


parent.mainloop()
