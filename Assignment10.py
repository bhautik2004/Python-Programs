f1=open("test1.txt","w")
f1.write("Today is the beautiful day")
f1.close()

f2=open("test1.txt","r")
txt=f2.readline()
print(txt)
f2.close()

f3=open("test1.txt","a")
f3.write("Tomorrow is the better future")
f3.close()

f4=open("test1.txt","r")
text=f4.read()
print(text)
