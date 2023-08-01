import sys
input=sys.stdin.readline
c=list()
n,m=map(int,input().split())
visited=[0 for _ in range(n+1)]
def dfs(st,depth): 
    global n,m    
    for x in range(st,n+1):
        if visited[x]==0:            
            c.append(x)
            #방문체크
            visited[x]=1
            #깊이에 도달하면 
            if depth==m:
                print(' '.join(map(str,c)))                
            #아직 깊이가 아니라면 재귀
            else:                
                dfs(x+1,depth+1)
            #이걸 실행할 때 쯤이면 깊이에 도달한 직후거나 return하면서 조건을 회수하는 중임
            c.remove(x)#pop을 사용해도 상관 없음                     
            #방문해제
            visited[x]=0
dfs(1,1)  