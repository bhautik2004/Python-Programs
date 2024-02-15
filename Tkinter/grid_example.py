from tkinter import *
p=Tk()
p.geometry("200x200")

name=Label(p,text="UserName").grid(row=0,column=0)
en=Entry(p).grid(row=0,column=1)

password=Label(p,text="Password").grid(row=1,column=0)
ep=Entry(p).grid(row=1,column=1)

loginbtn=Button(p,text="Login").grid(row=2,column=0)

p.mainloop()
