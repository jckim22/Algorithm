#아이디어:  이중 for 문으로 모든 노드에 대하여 1이면서 방문하지 않았으면 방문 ,방문 처리 할때마다 카운트 +1
#시간복잡도:  2중 for문 25*25*(DFS 25x25 + 4x25x25 시간 복잡도 충분) 최악의 경우 39,453,125 < 1억
#자료구조: int[][] : matrix , int[][]: 방문확인
import sys
input=sys.stdin.readline
n=int(input())
matrix=[list(map(int,input().strip())) for _ in range(n)]
visited=[[0 for _ in range(n)] for _ in range(n)]
cnt=0
def dfs(x,y,depth):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return
    #방문한 곳이면 리턴
    if visited[x][y]!=0:
        return
    #그림이 아니면 리턴
    if matrix[x][y]==0:
        return
    #범위를 넘었다면 리턴
    #그림의 일부분이라면 방문처리 후 다음 노드 탄색 
    visited[x][y]=1
    cnt+=1
    dfs(x+1,y,depth+1)
    dfs(x,y+1,depth+1)
    dfs(x-1,y,depth+1)
    dfs(x,y-1,depth+1)
    return
answer=[]
result=0
for x in range(n):
    for y in range(n):
        cnt=0
        #방문하지 않은 그림 노드에 대해 dfs시작
        if visited[x][y]==0 and matrix[x][y]!=0:
            dfs(x,y,0)
            result+=1    
            answer.append(cnt)
print(result)
answer=sorted(answer)
for x in answer:
    print(x)
        
    