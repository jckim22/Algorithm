r,c,n=map(int,input().split())
stage=[[0 for _ in range(c)] for _ in range(r) ]

for x in range(n):
    a,b = map(int,input().split())
    stage[a-1][b-1]=1

from collections import deque
def BFS(row,col):
    q = deque()
    q.append((row,col))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=1
    
    while q:
        currow,curcol = q.popleft()
        for mv in range(4):
            nrow=currow+dx[mv]
            ncol=curcol+dy[mv]
            if nrow<0 or nrow>=r or ncol<0 or ncol>=c:
                continue
            if stage[nrow][ncol]!=1:
                continue
            q.append((nrow,ncol))
            stage[nrow][ncol]=0
            cnt+=1
            
    return cnt
res=0
for x in range(r):
    for y in range(c):
        if stage[x][y]==1:
            stage[x][y]=0
            cur=BFS(x,y)                        
            if cur>res:
                res=cur                
print(res)                
                
            
    
    