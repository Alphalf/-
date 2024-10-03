boy, girl = [int(x) for x in input().split()]
B=87
G=85
sum=int(boy*B+girl*G)
average=sum/(boy+girl)
average1=('%.4f' % average)
print(average1)
