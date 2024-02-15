#Encoding of String
str="Bhautik"
encodedstring=""
startstr="snj"
endstr="jnf"
strlen=len(str)
newstr=""
firstchar=str[0]
if(strlen<3):
    encodedstring=str[::-1]
else:
  newstr=str.replace(firstchar,'')
  newstr+=firstchar
  encodedstr=startstr+newstr+endstr
print(encodedstr)



#decoding of String
estr="snjhautikBjnf"
decodedstring=""
dstr=dstr=estr[3:-3]
lastchar=dstr[len(dstr)-1]
if(strlen<3):
    decodedstring=dstr[::-1]
else:
    newstr=str.replace(lastchar,'')
    decodedstring=lastchar+newstr

print(decodedstring)
    
    
    
    
