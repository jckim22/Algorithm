from sys import stdin
from collections import deque

n,l,r = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def BFS(row,col,visit):
    q=deque()
    q.append((row,col))
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    #시작 국가 방문처리
    visited[row][col]=1-visit
    uni=[]
    #시작 국가를 연합에 넣음
    uni.append([arr[row][col],row,col])
    while q:        
        ro,co=q.popleft()
        #bfs로 탐색        
        for i in range(4):     
            nr=ro+dx[i]
            nc=co+dy[i]
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            #국가간의 인구수 차이가 l과 r사이고 방문하지 않았다면 연합에 넣어준다(국경선을 오픈함)
            a=abs(arr[nr][nc]-arr[ro][co])              
            if r>=a and a>=l and visited[nr][nc]==visit:
                uni.append([arr[nr][nc],nr,nc])
                q.append((nr,nc))
                visited[nr][nc]=1-visit                
            else:
                continue
    #연합을 리턴                     
    return uni
#연합의 인구 이동 함수
def move(uni):
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
#연합 수가 1이면 반복 종료(연합 없음)
while mx>1:
    visit=1-visit
    mx=0
    #연합의 모임리스트
    unis=list()
    for x in range(n):
        for y in range(n):
            if visited[x][y]==visit:
                #연합을 append해준다.        
                unis.append(BFS(x,y,visit))
    #국경선이 열려 그 날의 연합이 완성됐다면 인구이동 시작                
    for x in range(len(unis)):
        cnt=move(unis[x])
        if cnt>mx:
            mx=cnt
    #인구이동이 있었다면 카운트            
    if mx>1:
        answer+=1     
print(answer)    
     