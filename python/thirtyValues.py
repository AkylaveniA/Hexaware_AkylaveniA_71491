arr=list(map(int,input().split()))
even=[]
odd=[]
pos=[]
neg=[]
zero=[]
for i in arr:
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)
    if i>0:
        pos.append(i)
    if i<0:
        neg.append(i)
    if i==0:
        zero.append(i)
print(f'even: {even}')
print(f'odd: {odd}')
print(f'pos: {pos}')
print(f'neg: {neg}')
print(f'zero: {zero}')
