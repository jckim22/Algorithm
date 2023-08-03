#아이디어
#리스트를 정렬한다.
#짝지었을 때는 사전순이 아님으로 순서 그대로 출력하면 될 것 같다.

from sys import stdin
input=stdin.readline
n,m = map(int,input().split())
num=list(map(int,input().split()))
num=sorted(num)
for x in range(len(num)):
    num[x]=[num[x],False]
result=[]
def dfs(depth):
    if depth==m:        
        print(' '.join(map(str,result)))
        return
    for x in range(len(num)):
        if not num[x][1]:            
            result.append(num[x][0])            
            num[x][1]=True
            dfs(depth+1)
            num[x][1]=False
            result.pop()
dfs(0)            