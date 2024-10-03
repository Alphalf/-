import math
m = int(input())
k = int(math.sqrt(m))
for i in range(2, k+2):
    if m % i == 0:
        break
if i == k+1: print("yes")
else: print("no")
