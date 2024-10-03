x=int(input())
k=x//4
y=x%4
if y==0:
    m=n=0
elif y==1:
    m=0
    n=1
    k-=1
elif y==2:
    m=1
    n=0
    k-=1
elif y==3:
    m=1
    n=1
    k-=2
print(m)
print(n)
print(k)
