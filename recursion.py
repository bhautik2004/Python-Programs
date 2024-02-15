def sum(lst):
    if not lst:
        return 0;
    else:
        return lst[0]+sum(lst[1:])
mylst=[1,2,3,4,5]
print(sum(mylst))
