import random
x=random.randint(1,100)
running=False
while not running:
    y=int(input("输入正确的数："))
    if y==x:
        print("正确")
        running=True
    elif y<x:
        print("偏小")
    else:
        print("偏大")

