from tkinter import *

def selectedoptions():
    selections = ""
    if c1var.get() == 0:
        selections += "option1\n"
    if c2var.get() == 1:
        selections += "option2\n"
    if c3var.get() == 1:
        selections += "option3"
    lable2.config(text=selections)

    
top = Tk()
c1var = IntVar()
c2var = IntVar()
c3var = IntVar()
checkb1 = Checkbutton(top, text="option1", variable=c1var, onvalue=0,offvalue=1)
checkb1.pack()
checkb2 = Checkbutton(top, text="option2", variable=c2var, onvalue=1, offvalue=0)
checkb2.pack()
checkb3 = Checkbutton(top, text="option3", variable=c3var, onvalue=1, offvalue=0)
checkb3.pack()
button1 = Button(top, text="Get Selections", command=selectedoptions)
button1.pack()
lable1 = Label(top, text="Selected Options : ")
lable1.pack(side="left")
lable2 = Label(top)
lable2.pack(side="left")

top.mainloop()

