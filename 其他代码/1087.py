def bubble_sort(a,n):
    for i in range(1,n):
        for j in range(n-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    bubble_sort(a,n)
    for x in a:
        print(x,end=' ')

