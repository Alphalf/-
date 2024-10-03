str=input()
flag=0
count=0
for i in str:
    if i==" ":
        flag=0
    else:
        if flag==0:
            flag=1
            count+=1
print(count)
