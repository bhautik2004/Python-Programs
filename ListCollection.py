#List collection in python:
list1=[1,2,3,4,5]
print("list1 =",list1)

#methods
list1.append(6)
print("list1.append(6) =" , list1)

list2=list1.copy()
print("list2=list1.copy() list2 = ", list2)

count=list1.count(2)
print("count=list1.count(2) =",count)

list1.insert(1,3)
print("list1.insert(1,3) = ",list1)

list1.pop(1)
print("list1.pop(1) =",list1)

ind=list1.index(4)
print("list1.index(4) =",ind)

list1.sort()
print("list1.sort() =",list1)

list2=['one','two','three']
print("list2 =",list2)

list2.remove("one")
print("list2.remove(\"one\") =",list2)

list1.extend(list2)
print("list1.extend(list2) =",list1)

list2.clear()
print("list2.clear() =",list2)


