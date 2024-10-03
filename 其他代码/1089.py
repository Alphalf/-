import math
def f(x):
    if x==2:
        return 1
    j=2
    while j<=math.sqrt(x) and x%j:
        j+=1
    if x%j==0:
        return 0
    return 1

if __name__=='__main__':
    n=int(input())
    s=0
    for i in range(2,n+1):
        if f(i):
            s+=1
    print(s)
