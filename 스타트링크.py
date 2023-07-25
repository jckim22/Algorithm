f,s,g,u,d = map(int,input().split())
visited=[0 for _ in range(1000001)]
from collections import deque
def bfs():
    q=deque()
    q.append(s)
    while q:    
        cur=q.popleft()
        if cur == g:
            print(visited[g])
            return
        move=[cur+u,cur-d]
        for mv in move:
            if mv>f or mv<1 or mv==cur:
                continue
            if visited[mv]>0 or mv==cur:
                continue
            q.append(mv)
            visited[mv]+=visited[cur]+1
    print('use the stairs')
    return
bfs()           
