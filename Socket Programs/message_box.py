from tkinter import *
from tkinter import messagebox

def clickfun():
    messagebox.showinfo("Success","Button Is Clicked...")

p=Tk()
p.geometry("300x200")
mes=Message(p,text="Click on Button ").pack()
clkbtn=Button(p,text="Click Me..",command=clickfun).pack()


p.mainloop()
