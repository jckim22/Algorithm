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
    for x in words:
        if checking(begin,x):
            q.append((x))
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