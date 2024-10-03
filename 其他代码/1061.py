for x in range(100//5+1):
    for y in range(100//3+1):
        for z in range(0,100*3+1,3):
            if 5*x+3*y+z/3==100 and x+y+z==100:
                print(x,y,z)
