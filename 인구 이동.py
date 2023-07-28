n,l,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
from collections import deque
def BFS(row,col,visit):
    q=deque()
    q.append((row,col))
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    visited[row][col]=1-visit
    uni=[]
    uni.append([arr[row][col],row,col])
    while q:        
        ro,co=q.popleft()        
        for i in range(4):     
            nr=ro+dx[i]
            nc=co+dy[i]
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            a=abs(arr[nr][nc]-arr[ro][co])
              
            if r>=a and a>=l and visited[nr][nc]==visit:
                uni.append([arr[nr][nc],nr,nc])
                q.append((nr,nc))
                visited[nr][nc]=1-visit                
            else:
                continue         
    return uni
def chogi(uni):
    sum=0
    for x in range(len(uni)):
        sum+=uni[x][0]
    ag=sum//len(uni)
    for x in range(len(uni)):
        a,b=uni[x][1],uni[x][2]        
        arr[a][b]=ag
    return len(uni)
    

answer=0
mx=2
visit=1
while mx>1:
    visit=1-visit
    mx=0
    unis=list()
    for x in range(n):
        for y in range(n):
            if visited[x][y]==visit:        
                unis.append(BFS(x,y,visit))
    for x in range(len(unis)):
        cnt=chogi(unis[x])
        if cnt>mx:
            mx=cnt
    if mx>1:
        answer+=1     
print(answer)    
     