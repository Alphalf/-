import math
s=int(input())
a=input().split()
a=map(int,a)
a=list(a)
for i in range(1,s):
    for j in range(s-i):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in a:
    print(i)
