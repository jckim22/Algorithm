from sys import stdin
N = int(stdin.readline())
K = int(stdin.readline())
cnt=0
A=1

while(N>K):
    R=N%2
    cnt+=R*A
    A*=2
    N//=2
    N+=R
    print(cnt,end=" ")
    print(N,end=" ")
    print(A, end=" ")
    print(R, end=" ")
    print()
print(cnt)
    