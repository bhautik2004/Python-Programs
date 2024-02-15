def Shell_Sort(array, a):
    gap = a // 2
    while gap > 0:
        for i in range(gap, a):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap //= 2
        
list1=[3,2,1,5,4]
a=len(list1)
Shell_Sort(list1,a)
print(list1)
            
