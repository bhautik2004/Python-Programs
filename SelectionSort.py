def selection_sort(lst):
    for i in range(0,len(lst)-1):
        minindex=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[minindex]:
                minindex=j
        lst[i],lst[minindex]=lst[minindex],lst[i]
list1=[4,1,3,5,2]
selection_sort(list1)
print(list1)
