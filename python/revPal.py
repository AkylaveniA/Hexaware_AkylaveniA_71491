str=input("enter string:")
print("reversed: ",end='')
rev=str[::-1]
print(rev)
if rev==str:
    print("is palindrome")
else:
    print("not palindrom")
