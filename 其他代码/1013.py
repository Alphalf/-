tou, jio = [int(x) for x in input().split()]
ji=0
tu=tou-ji
while ji*2+tu*4!=jio:
    ji=ji+1
    tu=tou-ji
print(str(ji)+" "+str(tu))
