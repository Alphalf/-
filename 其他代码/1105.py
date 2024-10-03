s=input()
t=''
for c in s:
    if c=='A':
        t+='T'
    if c=='T':
        t+='A'
    if c=='C':
        t+='G'
    if c=='G':
        t+='C'
print(t)
