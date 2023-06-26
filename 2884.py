from sys import stdin
a=list(map(int,stdin.readline().split()))
if a[1] < 45:
    if a[0]==0:
        a[0]+=24
    a[0]-=1
    a[1]=a[1]+60-45
    print(a[0],a[1])
else:
    a[1]=a[1]-45
    print(a[0],a[1])
    