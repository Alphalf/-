x=float(input())
s1=input()
s2=input()
tot=0
for i in range(len(s1)):
    if (s1[i])==s2[i]:
        tot+=1
if (tot/len(s1)>=x):
    print("yes")
else:
    print("no")
