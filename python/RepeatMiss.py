arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[2,3,5,6,7,2]
repeat=[]
miss=[]
arr1=set(arr1)
arr2=set(arr2)
for i in arr1:
    if i in arr2:
        repeat.append(i)
    else:
        miss.append(i)

print("repeating: ")
print(*repeat,sep=' ')
print("missing: ")
print(*miss,sep=' ')
