from random import randint
a={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
m=randint(1,10)
i=0;j=0;k=0;ans=""
while k!=3:
   i=i%10+1
   if a[i]==0:
       j+=1
   if j==m:
       a[i]=1
       k+=1
       j=0

       ans=ans+str(i)+" "
print(ans)

