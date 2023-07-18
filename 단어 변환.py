#depth로 계산 -----------------------
from collections import deque

#한 글자만 다른지 체킹
def checking(x,y):
    cnt=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            cnt+=1
    if cnt==1:
        return True
    return False
    
def BFS(begin,target,words):            
    q=deque()
    check=False
    #시작 단어와 시작 depth를 큐에 append(tuple)
    q.append((begin,0))
    #words에 target이 있는지 체킹
    for x in words:
        if x == target:
            check=True
    if not check:
        return 0
    
    while q:
        cur,depth=q.popleft()
        if cur==target:
            return depth
        #계속해서 넓은 범위로 탐색 수행, 그에 대한 깊이도 카운트
        for x in words:
            if checking(cur,x):
                q.append((x,depth+1))
                        
def solution(begin, target, words):

    return BFS(begin,target,words)

#방문처리 기법 사용 --------------------------------------

from collections import deque
#한 글자만 다른지 체킹
def checking(x,y):
    cnt=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            cnt+=1
    if cnt==1:
        return True
    return False
    
def BFS(begin,target,words,visited):            
    q=deque()
    check=False    
    #words에 target이 있는지 체킹
    for x in words:
        if x == target:
            check=True
    if not check:
        return 0
    for x in range(len(words)):
        if checking(begin,words[x]):
            q.append((words[x]))
            if not visited[x]:
                visited[x]+=1
    while q:
        cur=q.popleft()
        idx=words.index(cur)
        if cur==target:
            return visited[idx]
        #계속해서 넓은 범위로 탐색 수행, 그에 대한 깊이도 카운트
        for x in range(len(words)):
            if checking(cur,words[x]):
                q.append((words[x]))
                if not visited[x]:
                    visited[x]=visited[idx]+1
                        
def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    return BFS(begin,target,words,visited)