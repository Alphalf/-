s=input()
for i in range(1,4):
    sep=''
    empty=sep.join([" " for i in range(0,3-i)])
    str=sep.join([s for i in range(0,2*i-1)])
    print(empty,end="")
    print(str,end="")
    print(empty)
