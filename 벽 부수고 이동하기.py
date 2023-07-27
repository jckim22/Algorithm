# from collections import deque
# from itertools import combinations
# row,col=map(int,input().split())
# matrix=[list(map(int,input())) for _ in range(row)]
# walls=[]
# for x in range(row):
#     for y in range(col):
#         if matrix[x][y]==1:
#             walls.append([x,y])                    
# def BFS(ma):
#     q=deque()
#     q.append((0,0))
#     ma[0][0]=1
#     while q:
#         r,c=q.popleft()
#         dx=[-1,1,0,0]
#         dy=[0,0,-1,1]
#         for mv in range(4):
#             nr=r+dx[mv]
#             nc=c+dy[mv]
#             if nr<0 or nr>=row or nc<0 or nc>=col:
#                 continue
#             if ma[nr][nc]>0:
#                 continue
#             ma[nr][nc]=ma[r][c]+1
#             q.append((nr,nc))
#     return ma[row-1][col-1]

# min_distance=9999999        
# for wall in combinations(walls,1):  
#     for x in range(row):
#         for y in range(col):                        
#             matrix[x][y]=0
#     for x in walls:        
#         matrix[x[0]][x[1]]=1
#     matrix[wall[0][0]][wall[0][1]]=0
#     c=BFS(matrix)
#     if c!=0:
#         min_distance=min(c,min_distance)    
# if min_distance==9999999:
#     print(-1)
# else:
#     print(min_distance)
    
    
    
    

# from collections import deque
# row,col=map(int,input().split())
# matrix=[list(map(int,input())) for _ in range(row)]
# walls=[]
# for x in range(row):
#     for y in range(col):
#         if matrix[x][y]==1:
#             walls.append([x,y])                    
# def BFS(breakwall,ma):
#     q=deque()
#     q.append((0,0))
#     ma[0][0]=1
#     while q:
#         r,c=q.popleft()
#         dx=[-1,1,0,0]
#         dy=[0,0,-1,1]
#         for mv in range(4):
#             nr=r+dx[mv]
#             nc=c+dy[mv]
#             if nr<0 or nr>=row or nc<0 or nc>=col:
#                 continue
#             if nr==breakwall[0] and nc==breakwall[1]:
#                 ma[nr][nc]=ma[r][c]+1
#                 q.append((nr,nc))
#                 continue            
#             if ma[nr][nc]>0:
#                 continue
#             ma[nr][nc]=ma[r][c]+1
#             q.append((nr,nc))
#     return ma[row-1][col-1]
# min_distance=9999999    
# for x in walls:
#     matrixc=[mat[:] for mat in matrix]
#     c=BFS(x,matrixc)
#     if c!=0:
#         min_distance=min(min_distance,c)        
# if min_distance==9999999:
#     print(-1)
# else:
#     print(min_distance)






from collections import deque
row,col=map(int,input().split())
matrix=[list(map(int,input())) for _ in range(row)]
visited=[[[0 for _ in range(2)] for _ in range(col)] for _ in range(row)]

def bfs():
    q=deque()
    q.append([0,0,0])
    visited[0][0][0]=1
    while q:
        r,c,crush=q.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        if r==row-1 and c==col-1:
            print(visited[r][c][crush])
        for mv in range(4):
            nr=r+dx[mv]
            nc=c+dy[mv]            
            if nr<0 or nr>=row or nc<0 or nc>=col:
                continue
            if matrix[nr][nc]==1 and crush==0:
                visited[nr][nc][1]=visited[r][c][0]+1
                q.append([nr,nc,1])
            elif matrix[nr][nc]==0 and visited[nr][nc][crush]==0:
                visited[nr][nc][crush]=visited[r][c][crush]+1
                q.append([nr,nc,crush])
    return -1
print(bfs())
        
    
