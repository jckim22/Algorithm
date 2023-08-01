import sys
input=sys.stdin.readline
c=list()
n,m=map(int,input().split())
def dfs(depth): 
    global n,m    
    for x in range(1,n+1):        
        c.append(x)
        if depth==m:
            print(' '.join(map(str,c)))                
        else:                
            dfs(depth+1)
        c.pop()            
dfs(1)