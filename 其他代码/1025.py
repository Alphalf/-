s=int(input())
p=float(input())
if s<6:
    j=1.0
if s>=6 and s<=10:
    j=0.9
if s>=11:
    j=0.8
t=s*p*j
print("%.1f"%t)
