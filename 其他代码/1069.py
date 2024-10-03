k=[0.0325,0.03,0.03,0.02,0.0175]
money=int(input())
for i in range(5):
    money*=(k[i]+1)
print("%.2f"%(money))

