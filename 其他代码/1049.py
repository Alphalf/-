money=100000
year=0
while money>0:
    money=round(money*(1+0.037),2)-20000
    year+=1
print(year)
