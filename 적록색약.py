import sys
sys.setrecursionlimit(10**6)
n=int(input())
matrix=[list(input()) for _ in range(n)]
visited=[[0 for _ in range(n)] for _ in range(n)]
def dfs(x,y,c):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if visited[x][y]!=0:
        return False
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
for x in range(n):
    for y in range(n):
        if visited[x][y]==0:
            if dfs(x,y,matrix[x][y]):
                res+=1
for x in range(n):
    for y in range(n):
        if matrix[x][y]=='G':
            matrix[x][y]='R'
visited=[[0 for _ in range(n)] for _ in range(n)]     
for x in range(n):
    for y in range(n):
        if visited[x][y]==0:
            if dfs(x,y,matrix[x][y]):
                res2+=1            
print(res,res2)                



