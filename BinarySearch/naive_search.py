def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
#array = [2,3,4,6,7,8,10]
#target= int(input("Insert Array's value: "))

#finder = native_search(array,target)

#if finder!=-1:
#    print(f"Value found in position {finder} ")
#else:
#    print("No found")