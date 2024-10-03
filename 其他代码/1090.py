def max(x,y,z):
    if x<y:
        x=y
    if x<z:
        x=z
    return x

if __name__=='__main__':
    a,b,c=input().split()
    a,b,c=float(a),float(b),float(c)
    m=max(a,b,c)/(max(a+b,b,c)*max(a,b,b+c))
    print("%.3f"%(m))
