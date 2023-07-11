# import sys

# sys.setrecursionlimit(100000)

# def DFS(nx,ny):
#     #범위를 넘겼다면 리턴
#     if nx<0 or ny<0 or nx>=n or ny>=m:
#         return
#     #방문하지 않았다면
#     if farm[nx][ny]==1:
#         #방문처리 후
#         farm[nx][ny]=0
#         #상하좌우 DFS 진행
#         DFS(nx-1,ny)
#         DFS(nx+1,ny)
#         DFS(nx,ny-1)
#         DFS(nx,ny+1)
#         return True
#     return False

# t=int(input())
# for _ in range(t):
#     result=0
#     m,n,k=map(int,input().split())
#     farm=[[0]*m for _ in range(n)]
#     for _ in range(k):
#         a,b=map(int,input().split())
#         farm[b][a]=1
# #모든 노드에 DFS 진행            
#     for x in range(n):
#         for y in range(m):
#             #방문처리 과정을 수행해서 True를 리턴 받으면
#             if DFS(x,y):
#                 #카운트
#                 result+=1                
#     print(result)
    
from collections import deque

def BFS(x,y):
    q=deque()    
    q.append((x,y))
    if farm[x][y]==0:
        return
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if farm[nx][ny] == 0:
                continue
            if farm[nx][ny] == 1:
                farm[nx][ny]=0
                q.append((nx,ny))
                
    return True
    
        
    

    
t=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(t):
    result=0
    m,n,k=map(int,input().split())
    farm=[[0]*m for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        farm[b][a]=1
#모든 노드에 DFS 진행            
    for x in range(n):
        for y in range(m):
            #방문처리 과정을 수행해서 True를 리턴 받으면
            if BFS(x,y):
                #카운트
                result+=1                
    print(result)