from sys import stdin

N = int(stdin.readline())
S = list(map(int,stdin.readline().split()))
A = list()

for x in range(N):
    i = [x,S[x]]
    A.append(i)
A = sorted(A, key=lambda x: x[1])
cur=0
answer=0

for x in range(N):
    cur+=A[x][1]
    answer+=cur
    
print(answer)
    

