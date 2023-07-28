from collections import deque
startrow=0
startcol=0
fire=[]
row,col=map(int,input().split())
matrix=[list(input()) for _ in range(row)]
fire_visited=[[0 for _ in range(col)]  for _ in range(row)]
human_visited=[[0 for _ in range(col)]  for _ in range(row)]
#불과 사람의 시작위치 저장
for x in range(row):
    for y in range(col):
        if matrix[x][y]=='J':            
            startrow=x
            startcol=y
        if matrix[x][y]=='F':
            fire.append([x,y])
#불 BFS (일반적인 bfs)
def fire_bfs():
    q=[]
    q=deque()
    for x in fire:
        q.append([x[0],x[1]])
        fire_visited[x[0]][x[1]]=1
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    while q:
        r,c=q.popleft()        
        for mv in range(4):
            nr=r+dx[mv]
            nc=c+dy[mv]
            if nr<0 or nr>=row or nc<0 or nc>=col:
                continue
            if fire_visited[nr][nc]>0:
                continue
            if matrix[nr][nc]=='#':
                continue
            fire_visited[nr][nc]=fire_visited[r][c]+1
            q.append([nr,nc])
#사람 bfs (불이 도착한 시간보다 적을 때 q에 append하는 제약이 추가됨)                
def human_bfs():   
    q=[]     
    q=deque()
    q.append([startrow,startcol])
    human_visited[startrow][startcol]=1
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    while q:
        r,c=q.popleft()        
        for mv in range(4):
            nr=r+dx[mv]
            nc=c+dy[mv]
            if nr<0 or nr>=row or nc<0 or nc>=col:
                return human_visited[r][c]
                continue
            if human_visited[nr][nc]>0:
                continue
            if matrix[nr][nc]=='#' or matrix[nr][nc]=='F':
                continue
            if fire_visited[nr][nc]!=0:
                if human_visited[r][c]+1 >= fire_visited[nr][nc]:
                    continue
            human_visited[nr][nc]=human_visited[r][c]+1
            q.append([nr,nc])
    return 'IMPOSSIBLE'            
fire_bfs()    
print(human_bfs())