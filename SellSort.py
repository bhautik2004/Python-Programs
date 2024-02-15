def Shell_Sort(list1, a):
    gap = a // 2
    while gap > 0:
        for i in range(gap, a):
            temp = list1[i]
            j = i
            while j >= gap and list1[j - gap] > temp:
                list1[j] = list1[j - gap]
                j -= gap

            list1[j] = temp
        gap //= 2
        
list1=[3,2,1,5,4]
a=len(list1)
Shell_Sort(list1,a)
print(list1)
            
