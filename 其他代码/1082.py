def Area(a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s
L1,L2,L3,L4,L5=map(float,input().split())
S=Area(L1,L2,L5)+Area(L3,L4,L5)
print("%.2f" % S)

