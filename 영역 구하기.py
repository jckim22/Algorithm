import sys
sys.setrecursionlimit(10000000)

m,n,k=map(int,input().split())
stage=[[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    lx,ly,rx,ry=map(int,input().split())
    for x in range(ly,ry):
        for y in range(lx,rx):            
            stage[x][y]=2               
cnt=0
def DFS(nx,ny):    
    global cnt
    if nx<0 or nx>=m or ny<0 or ny>=n or stage[nx][ny]==1 or stage[nx][ny]==2:      
        return    
    stage[nx][ny]=1
    cnt+=1
    DFS(nx-1,ny)
    DFS(nx,ny-1)
    DFS(nx+1,ny)
    DFS(nx,ny+1)    
    return
import heapq
ans=[]
for x in range(m):
    for y in range(n):        
        DFS(x,y)        
        if cnt>0:            
            heapq.heappush(ans,cnt)
        cnt=0
ans.sort()
print(len(ans))
for x in ans:
    print(x, end=' ')    