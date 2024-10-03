for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if a**3+b**3+c**3==a*100+b*10+c:
                print(100*a+10*b+c)
