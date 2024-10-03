n=input()
num={}
for i in n:
    if i not in num:
        num[i]=0
    num[i]+=1
flag=False
for i in n:
    if num[i]==1:
        print(i)
        flag=True
        break
if not flag:
   print("no")
