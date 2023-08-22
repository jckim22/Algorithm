import sys
sys.setrecursionlimit(10**6)
n=int(input())
matrix=[list(input()) for _ in range(n)]
visited=[[0 for _ in range(n)] for _ in range(n)]
def dfs(x,y,c):
    #범위를 넘어가면
    if x<0 or x>=n or y<0 or y>=n:
        return False
    #방문했으면
    if visited[x][y]!=0:
        return False
    #같은 색깔이 아니면
    if matrix[x][y]!=c:
        return False
    visited[x][y]=1
    dfs(x-1,y,c)
    dfs(x,y-1,c)
    dfs(x+1,y,c)
    dfs(x,y+1,c)
    return True
res=0
res2=0
#첫번째 답 구하기
for x in range(n):
    for y in range(n):
        if visited[x][y]==0:
            if dfs(x,y,matrix[x][y]):
                res+=1
#G을 R와 같은 것으로 보기 위해 G를 R로 초기화                
for x in range(n):
    for y in range(n):
        if matrix[x][y]=='G':
            matrix[x][y]='R'
#그 에 따라 방문 여부도 초기화            
visited=[[0 for _ in range(n)] for _ in range(n)]     
#두번째 답 구하기
for x in range(n):
    for y in range(n):
        if visited[x][y]==0:
            if dfs(x,y,matrix[x][y]):
                res2+=1            
print(res,res2)                



