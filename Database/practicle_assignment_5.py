import mysql.connector as m
from tkinter import *
from tkinter import messagebox

con=m.connect(host="localhost",user="root",password="")
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS db1")
con.database='db1'
print("Database Created Successfully....")
cur.execute("CREATE TABLE IF NOT EXISTS student(rollno int(20),name varchar(50),mobile varchar(50),city varchar(50))")

def clearentry():
    rollno.delete(0,END)
    name.delete(0,END)
    mobile.delete(0,END)
    city.delete(0,END)
    
def insert():
    rn=rollno.get()
    nm=name.get()
    mn=mobile.get()
    cty=city.get()
    if(str(rn)=="" ):
        messagebox.showinfo("Error","Please Enter Roll No")
    elif(str(nm)==""):
        messagebox.showinfo("Error","Please Enter Name")
    elif(str(mn)==""):
        messagebox.showinfo("Error","Please Enter Mobile Number")
    elif(str(cty)==""):
        messagebox.showinfo("Error","Please Enter City")
    else:
        try:
            cur.execute(f"INSERT INTO student VALUES({rn},'{str(nm)}','{str(mn)}','{str(cty)}')")
            con.commit()
            messagebox.showinfo("Success","Record Inserted..")
            clearentry()
            
        except Exception as e:
            print(str(e))
            
def delete():
    rn=rollno.get()
    if(str(rn)=="" ):
        messagebox.showinfo("Error","Roll No is Required For Delete Record")
    else:
        try:
            cur.execute(f"DELETE FROM student WHERE rollno={rn}")
            con.commit()
            messagebox.showinfo("Success","Record Deleted..")
            clearentry()
        except Exception as e:
            print(str(e))
            
def update():
    rn=rollno.get()
    nm=name.get()
    mn=mobile.get()
    cty=city.get()
    if(str(rn)=="" ):
        messagebox.showinfo("Error","Please Enter Roll No")
    else:
        try:
            cur.execute(f"UPDATE student SET name='{str(nm)}',mobile='{str(mn)}',city='{str(cty)}' WHERE rollno={rn}")
            con.commit()
            messagebox.showinfo("Success","Record Updated..")
            clearentry()
        except Exception as e:
            print(str(e))

def select():
    rn = rollno.get()
    if str(rn) == "":
        messagebox.showinfo("Error", "Please Enter Roll No")
    else:
        try:
            cur.execute(f"SELECT * FROM student WHERE rollno={rn}")
            record = cur.fetchone()
            if record:
                clearentry()
                rollno.insert(0,record[0])
                name.insert(0,record[1])
                mobile.insert(0,record[2])
                city.insert(0,record[3])
                con.commit()
            else:
                messagebox.showinfo("Error", "No record found with the given Roll No")
        except Exception as e:
            print(str(e))

    

top=Tk()
top.geometry("350x200")
top.title("Student Registration Infromation")
Label(top,text="Roll No : ").place(x=40,y=10)
Label(top,text="Student Name : ").place(x=40,y=40)
Label(top,text="Mobile Number : ").place(x=40,y=70)
Label(top,text="City : ").place(x=40,y=100)

rollno=Entry(top)
name=Entry(top)
mobile=Entry(top)
city=Entry(top)

rollno.place(x=130,y=10)
name.place(x=130,y=40)
mobile.place(x=130,y=70)
city.place(x=130,y=100)

insertbtn=Button(top,text="Insert",command=insert)
insertbtn.place(x=50,y=130)
deletebtn=Button(top,text="Delete",command=delete)
deletebtn.place(x=110,y=130)
updatebtn=Button(top,text="Update",command=update)
updatebtn.place(x=170,y=130)
selectbtn=Button(top,text="Select",command=select)
selectbtn.place(x=240,y=130)
top.mainloop()



