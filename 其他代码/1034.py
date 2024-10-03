s=25
t=int(input(""))
v=s*3600/t
print(round(v,1))
if v<=100:
    print("正常")
elif v<120:
    print("超过规定时速且不足20%")
elif v<150:
    print("超过规定时速20%以上且不足50%")
elif v<170:
    print("超过规定时速50%以上且不足70%")
else:
   print("超过规定时速70%以上")
