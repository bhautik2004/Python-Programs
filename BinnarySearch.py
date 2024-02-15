def binary_search(lst,val):
    h=len(lst)
    l=0
    while l<h:
        mid=(l+h)//2
        midval=lst[mid]
        if midval==val:
            return f"Found At {mid}"
        elif midval<val:
            l=mid+1
        else:
            h=mid-1
    return False
list1=[1,2,3,4,5,6,7,8,9,10]
value=1
if binary_search(list1,value) != False:
    print(value,binary_search(list1,value))
else:
    print(value,"Not Found in list")
    
    
