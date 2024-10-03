n=int(input())
a=[False]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%i==0:
            a[j]=not a[j]
for i in range(1,n+1):
    if a[i]:
        print(i,end=' ')
