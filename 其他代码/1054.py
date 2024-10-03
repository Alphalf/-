num1,num2 = map(int, input().split())
m = max(num1, num2)
n = min(num1, num2)
r = m % n
while r != 0:
    m = n
    n = r
    r = m % n
print(n)
