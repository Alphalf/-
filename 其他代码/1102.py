n=int(input())
for i in range(n):
    a,b=input().split()
    if a[0]==b[0]:
        print("Tie")
    elif a[0]=='R' and b[0]=='S' or a[0]=='S' and b[0]=='P' or a[0]=='P' and b[0]=='R':
        print("Player1")
    else:
        print("Player2")
