n=int(input())
for i in range(n):
    s=input()
    c=s[0]
    if c>='a' and c<='z':
        t=c.upper()
    else:
        t=c
    for c in s[1:]:
        if c>='A' and c<='Z':
            t+=c.lower()
        else:
            t+=c
    print(t)
