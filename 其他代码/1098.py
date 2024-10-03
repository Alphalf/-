s1=input()
s2=input()
if s1.find(s2)!=-1:
    print("%s is substring of %s"%(s2,s1))
elif s2.find(s1)!=-1:
    print("%s is substring of %s"%(s1,s2))
else:
    print('No substring')
