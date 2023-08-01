# #아이디어:
# # dfs는 한번 돌림 처음 들어왔을 때 범위를 넘지 않고 방문하지 않았고 in set에 해당하지 않으면 방문체크 cnt+1-> 만난 알파벳을 set에 add -> 다음 탐색 시작 ->  끝을 만나면 depth를 append
# #시간복잡도:
# # v는 최대 400, e는 4x400, in은 list에서는 O(n)이지만 set에서는 O(1)의 수행시간을 가지고 있음 따라서 연산횟수는 2000남짓 ok
# #자료구조:
# # set-알파벳을 담을 집합, answer-depth를 담을 리스트, int[][] - visited, int [][] - matrix
# #아이디어:
# #set은 a~z로만 되어 있으므로 최악복잡도랑 직접적 상관은 없고,  O(1) 복잡도라고 해서 항상 빠른 건 아니고 비례상수가 클 수 있다는 걸 유념하자.
# #따라서 딕셔너리로 아이디어를 전환한다.
# #그리고 만났던 알파벳은 다시 갈 수 없기 때문에 굳이 방문처리도 필요 없다.
# #먼저 딕셔너리에 모든 알파벳을 초기화 -> 알파벳을 만났을 때 그 알파벳의 value가 0이 아니라면 return
# #시간복잡도
# #딕셔너리는 key로 찾기 때문에 O(1)이라고 볼 수 있다.abs
# #위에서 말한 dfs 시간에 O(1)의 오버헤드는 충분할 것으로 보인다.
# #자료구조:
# # dictionary-알파벳을 담을 해쉬맵, answer-depth를 담을 리스트, int [][] - matrix
# #아이디어:
# #딕셔너리는 copy함수에서 시간을 많이 소요해 시간초과가 생겼다.abs
# #그래서 list를 사용했지만 이번에는 메모리 초과가 났다.abs
# #딕셔너리가 시간초과를 통과했어도 메모리 초과가 생겼을 것이다.abs
# #복사하는 시간이 오래걸리고 공간복잡도도 매우 크다.
# #마지막으로 str으로 아이디어를 전환해본다.
# #만나는 알파벳을 str에 추가 이후 in으로 str에 그 알파벳이 존재하는지 여부를 확인한다.
# #시간복잡도
# #str에서 in은 매우 짧은 것으로 예상된다.abs
# #자료구조:
# # str[]:alpha, answer-depth를 담을 리스트, int [][] - matrix

# from collections import defaultdict
# import sys
# import gc
# input=sys.stdin.readline
# row,col=map(int,input().split())
# matrix=[input().strip() for _ in range(row)]
# answer=[]
# def dfs(r,c,depth,alpha):        
#     global answer
#     if r<0 or r>=row or c<0 or c>=col:
#         answer.append(depth)
#         return
#     if matrix[r][c] in alpha:
#         return
#     alpha+=matrix[r][c]
#     dfs(r-1,c,depth+1,alpha)
#     dfs(r,c-1,depth+1,alpha)
#     dfs(r,c+1,depth+1,alpha)
#     dfs(r+1,c,depth+1,alpha)    
# alpha=''
# dfs(0,0,0,alpha)
# print(max(answer))




# from collections import defaultdict
# import sys
# input=sys.stdin.readline
# row,col=map(int,input().split())
# matrix=[input().strip() for _ in range(row)]
# alpha=list()
# for x in range(65,91):
#     alpha.append(0)
# answer=[]
# def dfs(r,c,depth,alphas):        
#     global answer
#     if r<0 or r>=row or c<0 or c>=col:
#         answer.append(depth)
#         return
#     idx=ord(matrix[r][c])-65
#     if alphas[idx]!=0:
#         answer.append(depth)
#         return
#     alphas[idx]+=1 
#     dfs(r-1,c,depth+1,alphas[:])
#     alphas[idx]-=1 
#     alphas[idx]+=1 
#     dfs(r,c-1,depth+1,alphas[:])
#     alphas[idx]-=1 
#     alphas[idx]+=1 
#     dfs(r,c+1,depth+1,alphas[:])
#     alphas[idx]-=1 
#     alphas[idx]+=1 
#     dfs(r+1,c,depth+1,alphas[:])
#     alphas[idx]-=1 
    
# dfs(0,0,0,alpha[:])
# print(max(answer))



row,col=map(int,input().split())
matrix=[list(input()) for _ in range(row)]
alpha=set()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
answer=0
def dfs(r,c,depth):    
    global answer
    answer=max(answer,depth)    
    alpha.add(matrix[r][c])
    for mv in range(4):
        nr, nc = r + dx[mv], c + dy[mv]      
        if 0 <= nr < row and 0 <= nc < col:
            if matrix[nr][nc] not in alpha:
                dfs(nr, nc, depth + 1)
    #더 이상 갈 곳이 없어서 막혔다면 삭제
    alpha.remove(matrix[r][c])        

dfs(0,0,1)
print(answer)






row,col=map(int,input().split())
matrix=[list(input()) for _ in range(row)]
alpha=set()
answer=0
def dfs(r,c,depth):    
    global answer
    answer=max(answer,depth)
    if r<0 or r>=row or c<0 or c>=col:
        return    
    if matrix[r][c] in alpha:        
        return    
    alpha.add(matrix[r][c])    
    dfs(r-1,c,depth+1)
    dfs(r,c-1,depth+1)
    dfs(r,c+1,depth+1)
    dfs(r+1,c,depth+1)
    alpha.remove(matrix[r][c])

dfs(0,0,0)
print(answer)






####################################


#아이디어: dfs는 한번 돌림 처음 들어왔을 때 범위를 넘지 않고 방문하지 않았고 in set에 해당하지 않으면 방문체크 cnt+1-> 만난 알파벳을 set에 add -> 다음 탐색 시작 ->  끝을 만나면 depth를 append
#시간복잡도: v는 최대 400, e는 4x400, in은 list에서는 O(n)이지만 set에서는 O(1)의 수행시간을 가지고 있음 따라서 연산횟수는 2000남짓 ok
#자료구조:set-알파벳을 담을 함수, answer-depth를 담을 리스트, int[][] - visited, int [][] - matrix
import sys
input=sys.stdin.readline
row,col=map(int,input().split())
matrix=[input().strip() for _ in range(row)]
visited=[[0 for _ in range(col)] for _ in range(row)]
answer=[]
def dfs(r,c,depth,alpha):
    alpha=set(alpha)
    global answer
    if r<0 or r>=row or c<0 or c>=col:
        answer.append(depth)
        return
    if visited[r][c]==1:
        answer.append(depth)
        return
    if matrix[r][c] in alpha:
        answer.append(depth)
        return
    visited[r][c]==1
    alpha.add(matrix[r][c])
    alpha=list(alpha)
    dfs(r-1,c,depth+1,alpha[:])
    dfs(r,c-1,depth+1,alpha[:])
    dfs(r,c+1,depth+1,alpha[:])
    dfs(r+1,c,depth+1,alpha[:])
dfs(0,0,0,set())
print(max(answer))


#아이디어2

from collections import defaultdict
import sys
input=sys.stdin.readline
row,col=map(int,input().split())
matrix=[input().strip() for _ in range(row)]
alpha=defaultdict(int)
for x in range(97,123):
    alpha[chr(x)]
answer=[]
def dfs(r,c,depth,alphas):        
    global answer
    if r<0 or r>=row or c<0 or c>=col:
        answer.append(depth)
        return
    if alphas[matrix[r][c]]!=0:
        answer.append(depth)
        return
    alphas[matrix[r][c]]+=1
    dfs(r-1,c,depth+1,alphas)
    dfs(r,c-1,depth+1,alphas)
    dfs(r,c+1,depth+1,alphas)
    dfs(r+1,c,depth+1,alphas)
    
dfs(0,0,0,alpha.copy())
print(max(answer))


#아이디어3

from collections import defaultdict
import sys
input=sys.stdin.readline
row,col=map(int,input().split())
matrix=[input().strip() for _ in range(row)]
alpha=list()
for x in range(65,91):
    alpha.append(0)
answer=[]
def dfs(r,c,depth,alphas):        
    global answer
    if r<0 or r>=row or c<0 or c>=col:
        answer.append(depth)
        return
    idx=ord(matrix[r][c])-65
    if alphas[idx]!=0:
        answer.append(depth)
        return
    alphas[idx]+=1    
    
    dfs(r-1,c,depth+1,alphas[:])
    dfs(r,c-1,depth+1,alphas[:])
    dfs(r,c+1,depth+1,alphas[:])
    dfs(r+1,c,depth+1,alphas[:])
    
dfs(0,0,0,alpha[:])
print(max(answer))

#아이디어4

row,col=map(int,input().split())
matrix=[input() for _ in range(row)]
answer=0
def dfs(r,c,depth):    
    global answer
    answer=max(answer,depth)
    if r<0 or r>=row or c<0 or c>=col:
        return    
    if matrix[r][c] in alpha:        
        return    
    alpha.add(matrix[r][c])    
    dfs(r-1,c,depth+1)
    dfs(r,c-1,depth+1)
    dfs(r,c+1,depth+1)
    dfs(r+1,c,depth+1)
    alpha.remove(matrix[r][c])
alpha=set()
dfs(0,0,0)
print(answer)

#아이디어5
import sys
input=sys.stdin.readline
row,col=map(int,input().split())
matrix=[input().strip() for _ in range(row)]
answer=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(r,c,depth):    
    global answer
    answer=max(answer,depth)    
    for mv in range(4):
        nr=r+dx[mv]
        nc=c+dy[mv]        
        if nr<0 or nr>=row or nc<0 or nc>=col:                        
            continue
        if matrix[nr][nc] in alpha:                        
            continue
        alpha.add(matrix[nr][nc])
        dfs(nr,nc,depth+1)
    #더 이상 갈 곳이 없어서 막혔다면 삭제
    alpha.remove(matrix[r][c])        
alpha=set()
alpha.add(matrix[0][0])
dfs(0,0,1)
print(answer)

#아이디어6

import sys
input=sys.stdin.readline
row,col=map(int,input().split())
matrix=[list(input().strip()) for _ in range(row)]
answer=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(r,c,depth):    
    global answer
    answer=max(answer,depth)    
    for mv in range(4):
        nr=r+dx[mv]
        nc=c+dy[mv]        
        if nr<0 or nr>=row or nc<0 or nc>=col:                        
            continue
        if matrix[nr][nc] in alpha:                        
            continue
        alpha.add(matrix[nr][nc])
        dfs(nr,nc,depth+1)
    #더 이상 갈 곳이 없어서 막혔다면 삭제
    alpha.remove(matrix[r][c])        
alpha=set()
alpha.add(matrix[0][0])
dfs(0,0,1)
print(answer)