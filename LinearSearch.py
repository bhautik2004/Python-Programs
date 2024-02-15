def isfound(lst,val):
    for i in range(len(lst)):
        if(lst[i] == val):
            return f"Found At Index {i}"
    return "Not Found in List"
list1=[1,3,4,2,5]
value=int(input("Enter Number : "))
isfound=isfound(list1,value)
print(value,isfound)
