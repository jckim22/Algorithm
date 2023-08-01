#  1. 아이디어: 2충 for문 -> 방문 안되어 있고 1이면 -> BFS로 탐색 -> 방문처리 할 때마다 카운트 -> 카운트 반환
#  2. 시간복잡도: BFS(O(v+e)) v= 500*500 e=vx4 = 4x500x500  v+e = 125만 정ㄷ <1억,2억 OK
#  3. 자료구조 : int[][]: matrix, int[][]:  방문처리, queue: bfs
import sys
from collections import deque
input=sys.stdin.readline
row,col=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(row)]
visited=[[0 for _ in range(col)] for _ in range(row)]

def bfs(startrow,startcol):
    q=deque()
    q.append((startrow,startcol))
    cnt=0
    #시작 노드 방문처리
    visited[startrow][startcol]=1
    #방문처리 했으니 카운트
    cnt+=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        r,c=q.popleft()        
        for mv in range(4):
            nr=r+dx[mv]
            nc=c+dy[mv]
            if nr<0 or nr>=row or nc<0 or nc>=col:
                continue
            if visited[nr][nc]!=0:
                continue
            if matrix[nr][nc]==0:
                continue
            #방문처리
            visited[nr][nc]=1
            cnt+=1
            q.append((nr,nc))              
    return cnt            
maxw=0            
answer1=0
for x in range(row):
    for y in range(col):
        if visited[x][y]==0 and matrix[x][y]==1:    
            answer1+=1        
            maxw=max(maxw,bfs(x,y))            
print(answer1)
print(maxw)
            
            
            
            