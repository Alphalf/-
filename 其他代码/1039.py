l=int(input())
h=int(input())
if l>h:
    print("输入的下限应该小于上限")
else:
    for i in range(l,h):
        c=5*(i-32)/9
        if i<100:
            print(" "*6+str(i)+" "*5+str('%.2f'%c))
        else:
            print(" "*5+str(i)+" "*5+str('%.2f'%c))
