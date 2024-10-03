s=input()
f=s[::-1]
x=""
if f[-1]=="-":
    x="-"
    f=f[:-1]

while f[0]=="0" and len(f)>1:
    f=f[1:]
if x=="-":
    f="-"+f
print(f)
