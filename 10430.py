from sys import stdin
a = list(map(int,stdin.readline().split()))
print((a[0]+a[1])%a[2])
print(((a[0]%a[2])+a[1]%a[2])%a[2])
print((a[0]*a[1])%a[2])
print(((a[0]%a[2])*a[1]%a[2])%a[2])