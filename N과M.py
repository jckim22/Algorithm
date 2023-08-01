#아이디어
#for문을 n만큼반복 해당 수를 list에 넣고 다음 수가 list에 있는지 확인 후 없으면 list에 add, 만약 다 깊이에 도달한다면 사용한 요소를 삭제하면서 return
#시간복잡도
#백트랙킹은 중복이 가능할 때는  O(n^n)(n=8 까지 가능함), 중복이 불가능할 때는 O(n!)(n=10까지 가능함)의 수행시간을 갖는다.
#이 문제에서는 선택하면서 올라온 숫자들을 그 뒤에서는 선택하지 못하는 순열이므로 O(n!)의 시간복잡도를 갖게되고
#연산횟수는 대략 8!=40,320 정도로 보인다.
#n의범위가 작기 때문에 아무 문제없이 해결될 것으로 보임
#자료구조
#set은 탐색할 때 O(1)의 시간이 있어서 리스트보다 효율적이지만 순서가 상관없다는 점에서 출력에 문제가 생길 수 있다.abs
#이 문제는 list로 풀어도 시간복잡도에서 아무 문제가 없기 때문에 list로 풀겠다.
# import sys
# input=sys.stdin.readline
# c=list()
# n,m=map(int,input().split())
# def dfs(depth): 
#     global n,m    
#     for x in range(1,n+1):
#         if x not in c:
#             c.append(x)
#             #깊이에 도달하면 
#             if depth==m:
#                 print(' '.join(map(str,c)))            
#             #아직 깊이가 아니라면 재귀
#             else:
#                 dfs(depth+1)
#             #이걸 실행할 때 쯤이면 깊이에 도달한 직후거나 return하면서 조건을 회수하는 중임
#             c.remove(x)                
# dfs(1)    

import sys
input=sys.stdin.readline
c=list()
n,m=map(int,input().split())
visited=[0 for _ in range(n+1)]
def dfs(depth): 
    global n,m    
    for x in range(1,n+1):
        if visited[x]==0:
            c.append(x)
            #방문체크
            visited[x]=1
            #깊이에 도달하면 
            if depth==m:
                print(' '.join(map(str,c)))                
            #아직 깊이가 아니라면 재귀
            else:
                dfs(depth+1)
            #이걸 실행할 때 쯤이면 깊이에 도달한 직후거나 return하면서 조건을 회수하는 중임
            c.remove(x)#pop을 사용해도 상관 없음                
            #방문해제
            visited[x]=0
dfs(1)    
