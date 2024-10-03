def f(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
if __name__=='__main__':
    m,n=input().split()
    m,n=int(m),int(n)
    print(f(m)//f(m-n)//f(n))
