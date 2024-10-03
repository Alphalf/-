s=input()
flag=True
if s[0]>='0' and s[0]<='9':
    flag=False
for c in s:
    if c>='0' and c<='9':
        continue
    if c>='A' and c<='Z':
        continue
    if c>='a' and c<='z':
        continue
    if c=='_':
        continue
    flag=False
    break
if flag:
    print("yes")
else:
    print("no")

