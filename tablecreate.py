import mysql.connector as m

con=m.connect(host="localhost",user="root",password="",database="pydb")

cur=con.cursor()
try:
    cur.execute("CREATE TABLE IF NOT EXISTS user(id varchar(50),name varchar(50), age int(50))")
    print("Table Created Succesfully..")
    
    cur.execute("INSERT INTO user VALUES(1,'Bhautik',20)")
    print("Record inserted Successfully...")
    con.commit()
except Exception as e:
    print(str(e))

