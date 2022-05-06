n=list(map(int,input().split()))[:6]
n.sort()
print(f'max: {max(n)}')
print(f'second max: {n[-2]}')
print(f'min: {min(n)}')
