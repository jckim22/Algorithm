#아이디어:
#리스트 순서대로 백트랙킹을 진행한다.abs
#True,False로 사용 여부 체크
#0이 되면 cnt+1 후 return
#깊이가 전체 수열의 길이까지 왔는데 0이 되지 않았으면 return
#시간복잡도
#정수의 범위가 꽤 큰데 시간 초과가 나지 않을지 모르겠다.
#자료구조
#2차원 리스트:정수 모임과 방문체크


import sys
input=sys.stdin.readline
n,s=map(int,input().split())
num=list(map(int,input().split()))
for x in range(len(num)):
    num[x]=[num[x],False,x]
cnt=0
tmp=[]
def dfs(idx,depth,result,beforeidx,start):    
    global cnt
    if not start and result==s:                
        cnt+=1             
    start=False
    if depth==n:
        return
    for x in range(idx,len(num)):
        if not num[x][1] and beforeidx<=num[x][2]:
            result+=num[x][0]
            num[x][1]=True                                      
            tmp.append(num[x][0])            
            dfs(idx+1,depth+1,result,num[x][2],start)            
            tmp.pop()
            num[x][1]=False
            result-=num[x][0]
dfs(0,0,0,0,True)            
print(cnt)
        
