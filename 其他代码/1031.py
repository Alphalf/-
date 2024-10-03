age=int(input(""))
HRrest=float(input(""))
gender=str(input (""))
if gender=="male":
    n=220
else:
    n=210
low=(n-age-HRrest)*0.6+HRrest
high=(n-age-HRrest)*0.8+HRrest
print(str(low)+"~"+str(high))
