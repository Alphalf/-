n,m=input().split()
n=int(n)
m=int(m)
a=[False]*(n+1)
f,t,s=0,0,0
while f!=n:
    t+=1
    if t==n+1:
        t=1
    if a[t]==False:
        s+=1
    if s==m:
        s=0
        print(t,end=" ")
        a[t]=True
        f+=1
