def Merge_Sort(list1):
    if len(list1) > 1:
        #  mid is the point where the list1 is divided into two sublist1s
        mid = len(list1)//2
        Left = list1[:mid]
        Right = list1[mid:]

        Merge_Sort(Left)
        Merge_Sort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                list1[k] = Left[i]
                i += 1
            else:
                list1[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            list1[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            list1[k] = Right[j]
            j += 1
            k += 1
list1=[3,2,1,5,4]
Merge_Sort(list1)
print(list1)
            
