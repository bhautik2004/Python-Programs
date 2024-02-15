def bubble_sort(lst):
    for i in range(1,len(lst)):
        for j in range(len(lst)-i):
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j]=lst[j],lst[j+1]
list1=[555,2,6,4,1,8,4,2,6,9,755,4,3,4,5,6,7]
bubble_sort(list1)
print(list1)
