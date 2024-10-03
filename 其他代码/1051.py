x=int(input())
running=False
while not running:
    y=int(input(""))
    if y==x:
        print("正确")
        running=True
    elif y<x:
        print("偏小")
    else:
        print("偏大")
