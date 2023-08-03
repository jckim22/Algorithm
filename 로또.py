#아이디어
#모든 경우의 수를 구하되 이전에 인덱스보다 클 때만 통과시킨다.
from sys import stdin
input=stdin.readline
result=[]
def dfs(depth,beforeidx):
    if depth==6:
        print(' '.join(map(str,result)))
        return
    for x in range(1,len(num)):
        if not num[x][1] and beforeidx<=num[x][2]:
            num[x][1]=True
            result.append(num[x][0])
            dfs(depth+1,num[x][2])
            num[x][1]=False
            result.pop()
            
while(True):
    num=list(map(int,input().split()))    
    k=num[0]
    if k==0:
        break
    for x in range(1,len(num)):
        num[x]=[num[x],False,x]
    dfs(0,1)
    print()
    