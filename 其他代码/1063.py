a,b=map(int,input().split())
from math import sqrt
for i in range(a,b+1):
    x=2
    while x<=int(sqrt(i)) and i%x!=0:
        x+=1
    if x>int(sqrt(i)):
        print(i)
