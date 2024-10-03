import math
n=int(input())
target=[True]*(n+1)
target[1]=False
m=int(math.sqrt(n)+1)
for i in range(2,m):
    if target[i]:
        for j in range(2,n//i+1):
            target[i*j]=False
for i in range(2,n+1):
    if target[i]:
        print(i,end=" ")
