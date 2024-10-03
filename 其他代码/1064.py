n=int(input())
k=0
for i in range(1,n+1):
    r=1
    for j in range(1,i+1):
        r*=j
    k+=r
print(k%1000000)
