s=1
for i in range(2,15000,2):
    item=i*i/(i*i-1)
    s=s*item
pi=2*s
print('%.4f'%(pi))
