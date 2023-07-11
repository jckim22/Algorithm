def DFS(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    if graph[x][y]==0:        
        graph[x][y] = 1
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False
        

n,m = map(int,input().split())

graph = [list(map(int,input())) for x in range(n)]
result=0

for x in range(n):
    for y in range(m):
        if DFS(x,y):
            result+=1
            
print(result)
