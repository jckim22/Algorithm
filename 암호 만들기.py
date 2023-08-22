#아이디어:
# 1.알파벳들을 먼저 정렬한다.
# 2. 그 후 알파벳 순서에 대응하는 리스트를 만들고 False로 초기화한다.
# 3. 모음과 자음을 세면서 백트랙킹을 돌린다.
# 4. 방문을 안했고 이전 알파벳보다 순서가 뒤라면 방문처리한다.
# 5. 자음이 1개이상 모음이 2개 이상 깊이가 c가 되면 문자열을 출력한다.
#시간복잡도
#n이 12정도 되는 것 같다. 시간에 따라서 될 수도 있고 안 될수도 있을 것 같다.
#자료구조
#1차원 리스트:알파벳 & 방문확인리스트, set:모음 집합(set의 탐색은 O(1))

from sys import stdin
input=stdin.readline
l,c = map(int,input().split())
alpha=list(input().strip().split())
alpha=sorted(alpha)
for x in range(c):
    alpha[x]=[alpha[x],x]
visited=[False for _ in range(c)]
mo,za=0,0
s=''
#모음 집합
mos=set(['a','e','i','o','u'])
def dfs(st,d,beforeidx):
    global mo,za    
    #문자열의 길이가 L이고 모음과 자음의 조건이 충족되었다면
    if len(st)==l:
        if mo>=1 and za>=2:
            print(st)
        return
    for x in range(d,c):
        #방문하지 않았고 이전 방문 알파벳보다 현재 알파벳의 숫자가 높다면
        if not visited[x] and alpha[x][1]>=beforeidx:
            #모음일 때
            if alpha[x][0] in mos:
                visited[x]=True
                mo+=1
                st+=alpha[x][0]
                dfs(st,d+1,alpha[x][1])
                mo-=1
                visited[x]=False
                st=st[:-1]
            #자음일 때
            else:
                visited[x]=True
                za+=1
                st+=alpha[x][0]
                dfs(st,d+1,alpha[x][1])
                za-=1
                visited[x]=False
                st=st[:-1]
dfs(s,0,-1)            


