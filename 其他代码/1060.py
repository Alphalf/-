x=1
while True:
    n=x*x
    x+=1
    if n<1000:
        continue
    if n>9999:
        break
    max=n//100
    min=n%100
    if max//10==max%10 and min//10==min%10:
        print(n)


