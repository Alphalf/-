n=int(input())
a=input().split()
a=map(int,a)
a=list(a)
max=a[0]
b=0
for i in range(n):
    if a[i]>max:
        max=a[i]
        b=i
print(b+1)
