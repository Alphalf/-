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
    for x in range(6,101,2):
        for i in range(2,x//2+1):
            if f(i) and f(x-i):
                print("%d=%d+%d"%(x,i,x-i))
                break
