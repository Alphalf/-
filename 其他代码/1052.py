from math import sqrt
a=1
b=0
k=1
while k>0.00000001:
    b=b+k
    a=a+1
    k=1/(a*a)
pi=sqrt(6*b)
print('%.4f'%(pi))
