#아이디어 : 각각의 연결된 노드를 그래프로 구현했을 때 사이클이 생긴다면 정답이됨
            #사이클이 생기면 정답 리스트에 중복제거 후 튜플 형태로 append
            #모든 노드에 대하여 검사해야함으로 n번 dfs함
            #visited를 얕은 복사해서 dfs할 때마다 방문 기록을 초기화
            #결국 모든 노드가 돌고 돌이 싸이클에 도달할 것임            
#시간 복잡도 : n * v * e n은 100이고 따라서 v도 100이고 e는 2x100 이다. 따라서 2백만에 연산 횟수가 예상이 되는데 이는 1억에 한참 못 미친다.
#자료구조 : int[2][n] : graph, visited[n]: 방문확인, list(set()):answer
n=int(input())
graph=[]
#graph에 첫번째 줄과 두번째 줄로 2차원리슽로 만듬
for x in range(n):
    b=int(input())
    graph.append([x,b-1])
#방문횟수를 체크할 리스트
visited=[0 for _ in range(n)]
answer=[]
def dfs(x,visit):    
    #방문을 안했다면 방문체크
    if visit[x]==0:
        visit[x]=1        
    #방문한 곳에 돌아왔다면 싸이클이므로 정답에 넣어줌
    else:
        #[2,0]과 [0,2]는 같은 것이므로 set으로 중복제거 후 hashable한 tuple로 형변환
        answer.append(tuple(set(graph[x])))
        return            
    #방문체크하고 연결된 노드로 이동
    dfs(graph[x][1],visit)
#1번부터 n번까지 각각을 출발점으로 dfs를 진행
for x in range(0,n):    
    dfs(x,visited[:])
#아까 tuple로 받았기 떄문에 2차원리스트도 tuple로 바꾸고 set으로 중복제거    
answer=list(set(tuple(answer)))
result=[]
#결과값 append하고
for x in answer:
    for y in list(x):
        result.append(y)
#마지막 중복제거 (집합이기 떄문에)        
result=list(set(result))
#정렬
result=sorted(result)        
print(len(result))
for x in result:
    print(x+1)
    
    
    