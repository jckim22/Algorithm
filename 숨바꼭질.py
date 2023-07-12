from sys import stdin
from collections import deque
def BFS(x,depth):
    q=deque()    
    q.append(x)
    if n==k:
        print(0)        
        return
    while q:
        su=q.popleft()
        move=[su+1,su-1,2*su]
        if su==k:  
            print(visited[su])          
            break
        
        for m in move:
            if m<0 or m>100000:
                continue            
            if not visited[m]:
                q.append(m)                
                visited[m]=visited[su]+1
            
                        

n,k = map(int,stdin.readline().split())
visited=[0 for _ in range(100001)]

BFS(n,0)
