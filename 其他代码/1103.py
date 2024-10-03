a=input()
n=len(a)
a=a+a[0]
b=''
for i in range(n):
    x=ord(a[i])+ord(a[i+1])
    b=b+chr(x)
print(b)
