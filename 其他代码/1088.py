def sum(x):
    s=0
    for i in range(1,x):
        if x%i==0:
            s+=i
    return s

if __name__=='__main__':
    n=int(input())
    for i in range(2,n+1):
        if sum(i)==i:
            print(i)
