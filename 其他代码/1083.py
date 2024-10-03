def lcm(a, b):
    for i in range(min(a,b),0,-1):
        if a % i ==0 and b % i == 0:
            return a*b//i
num1,num2=map(int,input().split())
print(lcm(num1, num2))
