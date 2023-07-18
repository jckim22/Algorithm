n,k=map(int,input().split())
visited = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]
import sys

sys.setrecursionlimit(100000)

from collections import deque
def BFS():
    q=deque()
    q.append(n)
    while q:
        su=q.popleft() 
        move = [su-1,su+1,su*2]
        if su == k:
            return
        for mv in move:
            if mv>100000 or mv<0:
                continue
            if visited[mv]>0:
                continue
            q.append(mv)
            visited[mv]=visited[su]+1
            path[mv]=su
BFS()            
print(visited[k]) 
a=k
b=[]
b.append(k)
for _ in range(visited[k]):
    b.append(path[a])
    a=path[a]
print(' '.join(map(str,b[::-1])))
   
# visited = [0 for _ in range(100001)]              
# def DFS(su):
#     if su<0 or su>100000:
#         return
#     if su==k:
#         print(su)
#         return su
#     if visited[su]==0:
#         visited[su]=1
#         DFS(su-1)
#         DFS(su+1)
#         DFS(su*2)

# DFS(n)        

