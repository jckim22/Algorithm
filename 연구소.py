#아이디어:
#n=64 정도 된다.
#63c3 으로 백트랙킹을 떠올릴 수 있을 것 같다.
#안전한 좌표들을 다 저장하고 그 중 벽 3개를 골라서 bfs를 수행한다.
#시간복잡도
#깊이가 깊어봤자 3이기 때문에 충분히 가능할 것 같다.
#63c3 은 41664이고 bfs는 대략 64*4*64로 16385번의 연산수행횟수를 수행한다.
#41664 * 16385는 682,664,640 정도 되는데 시간 안에 해결이 어려울 수도 있겠다.
from collections import deque
from sys import stdin
def bfs(matrixx):    
    q=deque()        
    for x in virus:
        q.append(x)
    dx=[-1,1,0,0]    
    dy=[0,0,1,-1]
    while q:
        r,c=q.popleft()        
        for x in range(4):
            nr=r+dx[x]
            nc=c+dy[x]
            if nr>=n or nr<0 or nc>=m or nc<0:
                continue
            if matrixx[nr][nc]==2 or matrixx[nr][nc]==1:            
                continue            
            matrixx[nr][nc]=2
            q.append([nr,nc])
    a=checkSafe(matrixx)
    return a

            
def checkSafe(matrixxx):
    cnt=0
    for x in range(n):
        for y in range(m):
            if matrixxx[x][y]==0:
                cnt+=1
    return cnt                                
    
input=stdin.readline
n,m=map(int,input().split())
safe=[]
matrix=[list(map(int,input().split())) for _ in range(n)]
virus=[]

for x in range(n):
    for y in range(m):
        if matrix[x][y]==0:
            safe.append([x,y])
        if matrix[x][y] == 2:
            virus.append([x,y])
answer=0                  
import copy                     
def back(depth,idx):
    global answer    
    if depth == 3: 
        tmp=[mat[:] for mat in matrix]            
        answer=max(bfs(tmp),answer)                
        return
    for x in range(idx,len(safe)):
        matrix[safe[x][0]][safe[x][1]]=1
        back(depth+1,x+1)
        matrix[safe[x][0]][safe[x][1]]=0
back(0,0)
print(answer)
    



    
    
