s=input()
t=''
for c in s:
    if c>='a' and c<='z':
        t+=c.upper()
    else:
        t+=c
print(t)
