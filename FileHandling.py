#Write

file=open("one.txt","w")
file.write("Hello There!\n this is sample text document file\n")
file.close()
print("File Writen Successfully..")


#Read
'''
file=open("one.txt","r")
filetext=file.read()
print(filetext)
file.close()
'''

#Append
'''
file=open("one.txt","a")
file.write("this is another line add using append method")
print("file append successfully...")
file.close()
'''


