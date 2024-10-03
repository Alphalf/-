def factorial_function(x):
    a=1
    for i in range(2,x+1):
        a=a*i
    return a
sum=factorial_function(7)+factorial_function(11)-factorial_function(10)
print(sum)
