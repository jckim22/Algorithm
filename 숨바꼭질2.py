from sys import stdin
from collections import deque
n,k = map(int,stdin.readline().split())
visited = [0 for _ in range(1000001)]
cnt=0

if n==k:
    print(0)
    print(1)
    exit()

def BFS():
    global cnt
    q=deque()
    q.append(n)        
    
    while q:
        su=q.popleft()
        move=[su+1,su-1,su*2]        
        if su==k:
            cnt+=1      
        for mv in move:
            if mv>100000 or mv<0:
                continue
            if visited[mv] != 0 and visited[mv]!=visited[su]+1:
                continue
            else:
                visited[mv]=visited[su]+1
                q.append(mv)
BFS()
    
print(visited[k])
print(cnt)