import mysql.connector as m

conn=m.connect(host="localhost",user="root",password="")
cur=conn.cursor()
cur.execute("CREATE DATABASE pydb")
