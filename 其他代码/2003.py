for i in range(1,7):
    for j in range(1,7):
        if j <= i:
            print(j, end ="")
        else:
            print("", end ="")
    print()