from tkinter import *
from tkinter import messagebox

def getresult():
    python=pythonmark.get()
    android=androidmark.get()
    dw=dwmark.get()
    project=projectmark.get()
    totalm = int(python)+int(android)+int(dw)+int(project)
    totalmarks.config(text=str(totalm))
    pr=totalm/4
    prr=str(pr)+"%"
    percentage.config(text=prr)
    if pr>=70 and pr<=100:
        grade="A"
    elif pr>=50 and pr<=69:
        grade="B"
    elif pr>=35 and pr<49:
        grade="C"
    elif pr>=0 and pr<=34:
        grade="F"
    gradee.config(text=grade)
    
    if int(python)<28 or int(android)<28 or int(dw)<28 or int(project)<28:
        result.config(text="Fail")
    else:
        result.config(text="Pass")

p=Tk()
p.title("Marksheet")
p.geometry("600x200")

nameL=Label(p,text="Name:").grid(row=0,column=0)
name=Entry(p).grid(row=0,column=1)

rollnoL=Label(p,text="Roll No:").grid(row=2,column=0)
rollno=Entry(p).grid(row=2,column=1)

seatnoL=Label(p,text="Seat No:").place(x=350)
seatno=Entry(p).place(x=400)

srnoL=Label(p,text="Sr.No").grid(row=3,column=0)
srno1L=Label(p,text="1").grid(row=4,column=0)
srno2L=Label(p,text="2").grid(row=5,column=0)
srno3L=Label(p,text="3").grid(row=6,column=0)
srno4L=Label(p,text="4").grid(row=7,column=0)

subjectL=Label(p,text="Subject").grid(row=3,column=1)
subject1L=Label(p,text="Python").grid(row=4,column=1)
subject2L=Label(p,text="Android").grid(row=5,column=1)
subject3L=Label(p,text="DW").grid(row=6,column=1)
subject4L=Label(p,text="Project").grid(row=7,column=1)

submitbtn=Button(p,text="Submit",bg="blue",fg="white",command=getresult).grid(row=8,column=1)

marksL=Label(p,text="Marks").grid(row=3,column=2)
pythonmark=Entry(p)
pythonmark.grid(row=4,column=2)
androidmark=Entry(p)
androidmark.grid(row=5,column=2)
dwmark=Entry(p)
dwmark.grid(row=6,column=2)
projectmark=Entry(p)
projectmark.grid(row=7,column=2)

totalmarksL=Label(p,text="Total Marks").grid(row=4,column=3)
percentageL=Label(p,text="Percentage").grid(row=5,column=3)
gradeL=Label(p,text="Grade").grid(row=6,column=3)
resultL=Label(p,text="Result").grid(row=7,column=3)

totalmarks=Label(p,text="-")
totalmarks.grid(row=4,column=4)
percentage=Label(p,text="-")
percentage.grid(row=5,column=4)
gradee=Label(p,text="-")
gradee.grid(row=6,column=4)
result=Label(p,text="-")
result.grid(row=7,column=4)

p.mainloop()
