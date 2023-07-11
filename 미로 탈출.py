from collections import deque

def BFS(x,y):
    q=deque()
    q.append((x,y))        

    #큐가 빌 때까지 반복
    while q:
        #큐에서 검사할 노드를 꺼낸다.
        x,y = q.popleft()
        #인접한 4방향 모두 검사
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 초과시 
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #장애물이 있을시
            if graph[nx][ny]==0:
                continue
            #처음 방문한 노드라면
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
                
    return(graph[n-1][m-1])
            

n,m=map(int,input().split())
graph=[list(map(int,input())) for x in range(n)]
#상하좌우 방향벡터
dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(BFS(0,0))
