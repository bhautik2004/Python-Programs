from tkinter import *
p=Tk()
p.geometry("300x200")

name=Label(p,text="UserName :").place(x=20,y=30)
en=Entry(p).place(x=90,y=30)

password=Label(p,text="Password").place(x=20,y=60)
ep=Entry(p).place(x=90,y=60)

loginbtn=Button(p,text="Login").place(x=90,y=90)

p.mainloop()
