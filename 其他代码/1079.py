def factorial_function(x):
    a=1
    for i in range(2,x+1):
        a=a*i
    return a
n=int(input())
sum=factorial_function(n)
print(sum)
