s=input()
t=''
for c in s:
    if c>='A' and c<'Z' or c>='a' and c<'z':
        t+=chr(ord(c)+1)
    elif c=='Z':
        t+='A'
    elif c=='z':
        t+='a'
    else:
        t+=c
print(t)
