str=input().lower()
vowels=[]
consonant=[]

for i in str:
    if(i in "aeiou"):
        vowels.append(i)
    elif i!=' ':
        consonant.append(i)
print("vowels: ",sep=" ")
print(*vowels,sep=",")
print("consonant: ",sep=" ")
print(*consonant,sep=",")
