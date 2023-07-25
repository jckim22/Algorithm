# from collections import deque
# m,n=map(int,input().split())
# stage=[list(map(int,input().split())) for _ in range(n)]
# res=0
# def bfs():
#     global res
#     q=deque()
#     #처음 스테이지에서 익은 토마토의 좌표를 큐에 넣어준다
#     for x in range(n):
#         for y in range(m):
#             if stage[x][y]==1:
#                 q.append([x,y]) 
#     dx=[-1,1,0,0]
#     dy=[0,0,-1,1]        
#     while q:
#         arr=[]
#         #큐에 들어있는 좌표들을 배열에 append 해준다.
#         for i in range(len(q)):
#             x,y=q.popleft()    
#             arr.append([x,y])
#         #배열에 들어 있는 모든 좌표들로 bfs진행
#         #한 턴이 끝나면 한 depth가 끝난 것이므로 count+1
#         for i in arr:
#             x,y=i[0],i[1]            
#             for i in range(4):
#                 nx=x+dx[i]
#                 ny=y+dy[i]
#                 if nx<0 or nx>=n or ny<0 or ny>=m:
#                     continue
#                 if stage[nx][ny]==1 or stage[nx][ny]==-1:
#                     continue
#                 stage[nx][ny]=1
#                 q.append([nx,ny])        
#         res+=1
# bfs()
# #만약 bfs를 거치고도 익지 않은 토마토가 있다면 -1을 출력
# for x in range(n):
#     for y in range(m):
#         if stage[x][y]==0:
#             print(-1)
#             exit()
# print(res-1)


from collections import deque
m,n=map(int,input().split())
stage=[list(map(int,input().split())) for _ in range(n)]
def bfs():
    q=deque()
    #처음 스테이지에서 익은 토마토의 좌표를 큐에 넣어준다
    for x in range(n):
        for y in range(m):
            if stage[x][y]==1:
                q.append([x,y]) 
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]        
    while q:
        x,y=q.popleft()            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if stage[nx][ny]>=1 or stage[nx][ny]==-1:
                continue
            stage[nx][ny]=stage[x][y]+1
            q.append([nx,ny])                
bfs()
res=0
for x in stage:
    for y in x:
        if y==0:
            print(-1)
            exit()
    res=max(res,max(x))
print(res-1)    