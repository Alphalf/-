def f(a,b):
    m,n=a,b
    while n:
        m,n=n,m%n
    a//=m
    b//=m
    print(a,b)

if __name__=='__main__':
    a,b=input().split()
    a=int(a)
    b=int(b)
    f(a,b)

