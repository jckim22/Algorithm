from sys import stdin
n,k=map(int,stdin.readline().split())
visited = [0 for _ in range(100001)]
check = [False for _ in range(100001)]
if n==k:
    print(0)
    exit()
from collections import deque

def BFS():
    q=deque()
    q.append(n)
    while q:
        su=q.popleft()
        move = [su*2,su-1,su+1]
        if su==k:                
            return
        for mv in move:
            if mv<0 or mv>100000:
                continue
            if check[mv]:
                continue
            check[mv]=True
            if mv==su*2:
                visited[mv]=visited[su]
                q.append(mv)
            else:
                visited[mv]=visited[su]+1
                q.append(mv)
                    
BFS()                    
print(visited[k])