#아이디어
#N=6이라면
#0번부터 시작해서 팀 리스트에 넣는다.
#depth가 n/2이라면 한 팀을 결성한 것이므로 자동적으로 나머지 팀이 결정된다.
#그 뒤 팀 능력치를 계산한 뒤 차를 구해 리턴한다.
#돌아오면서 리스트에서 삭제해준다.
#시간복잡도
#백트랙킹이라 잘 가늠이 되지는 않는다.
#N이 4-20R까이지고 짝수만 들어오기 때문에 4,6,8,10,12,14,16,18,20 총 9가지이다.abs
#O(n!)를 생각하면 가능해보인다.
#자료구조
#1차원 리스트:스타트팀 링크팀, 2차원 행렬 리스트:각 선수들의 케미
from sys import stdin
input=stdin.readline
start=set()
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
person=[True]*n
def abil():    
    starttmp=0
    linktmp=0
    for x in range(n):
        for y in range(x,n):
            if x in start and y in start:       
                starttmp+=matrix[x][y]+matrix[y][x]
            elif x not in start and y not in start:
                linktmp+=matrix[x][y]+matrix[y][x]
    return abs(starttmp-linktmp)            
answer=10000000    
def dfs(depth):
    global answer
    if depth==int(n/2):
        answer=min(answer,abil())
        return
    for x in range(n):
            if person[x]:
                start.add(x)
                person[x]=False
                dfs(depth+1)
                start.remove(x)                
                person[x]=True                
dfs(0)
print(answer)                


from sys import stdin
input=stdin.readline
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
person=[True]*n
def abil():    
    starttmp=0
    linktmp=0
    for x in range(n):
        for y in range(x,n):
            if not person[x] and not person[y]:
                starttmp+=matrix[x][y]+matrix[y][x]
            elif person[x] and person[y]:
                linktmp+=matrix[x][y]+matrix[y][x]    
    return abs(starttmp-linktmp)            
answer=10000000    
def dfs(depth):
    global answer
    if depth==int(n/2):
        answer=min(answer,abil())
        return
    for x in range(n):
            if person[x]:                
                person[x]=False
                dfs(depth+1)                
                person[x]=True                
dfs(0)
print(answer)    


import sys
n = int(sys.stdin.readline())
matrix = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
person = [ False for _ in range(n) ] #1
answer = sys.maxsize #2   
def dfs(depth,idx):
    global answer
    if depth==n//2:
        starttmp,linktmp=0,0
        for x in range(n):
            for y in range(n):
                if person[x] and person[y]:
                    starttmp+=matrix[x][y]
                elif not person[x] and not person[y]:
                    linktmp+=matrix[x][y]
        answer=min(answer,abs(starttmp-linktmp))    
        return
    for x in range(idx,n):
        if not person[x]:                
            person[x]=True
            dfs(depth+1,idx+1)                
            person[x]=False
dfs(0,0)
print(answer)   