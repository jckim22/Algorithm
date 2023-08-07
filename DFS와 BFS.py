#아이디어
#정점의 개수를 기준으로 각각 간선을 통해 이어져 있는 그래프의 형태를 만든다.abs
#정점은 인덱스로 한다.abs
#시간복잡도
#정점은 1,000개 간선은 1,0000개 까지의 범위가 있으므로 O(v*e)로 10,000,000의 연산횟루를 갖게 된다. okay
n,m,v = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
for x in range(m):
    graph[edge[x][0]].append(edge[x][1])
    graph[edge[x][1]].append(edge[x][0])
for x in range(len(graph)):
    graph[x]=sorted(graph[x])
from collections import deque
def bfs():
    q=deque()
    q.append(v)
    visited[v]=False
    print(v,end=' ')
    while q:
        curv=q.popleft()
        for x in graph[curv]:
            if not visited[x]:
                continue
            q.append(x)
            visited[x]=False
            print(x,end=' ')
def dfs(idx):
    if visited[idx]:
        return
    visited[idx]=True
    print(idx,end=' ')
    for x in graph[idx]:                
        dfs(x)
dfs(v)            
print()
bfs()

