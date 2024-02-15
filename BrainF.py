#Branin F**k
lst=[]
for i in range(101):
    lst.append(0)
    
userinput=input("Enter")
position=0
for i in userinput:
    if i == '+':
        lst[position]+=1
    elif i == '>':
        position+=1
    elif i == '.':
        for j in range(position+1):
            print(lst[j])

    
