per=[6,2,5,5,4,5,6,3,7,6]
aim=6
for num in range(112):
    target=0
    if num<10:
        target=per[num]
    elif num<100:
        target=per[num//10]+per[num%10]
    else:
        target=per[num//100]+per[num//10%10]+per[num%10]
    if target==aim:
       print(num)
