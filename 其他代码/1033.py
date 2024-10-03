height=float(input(""))
weight=float(input(""))
bmi=float(weight/height**2)
if bmi<18.5:
    print('%.1f'%bmi)
    print("偏瘦")
elif 18.5<=bmi<25:
    print('%.1f'%bmi)
    print("正常")
elif 25<=bmi<30:
    print('%.1f'%bmi)
    print("偏胖")
elif 30<=bmi<35:
    print('%.1f'%bmi)
    print("肥胖")
elif 35<=bmi<40:
    print('%.1f'%bmi)
    print("重度肥胖")
else:
    print('%.1f'%bmi)
    print("极度肥胖")
