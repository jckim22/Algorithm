import sys
input=sys.stdin.readline
c=list()
n,m=map(int,input().split())
def dfs(st,depth): 
    global n,m    
    for x in range(st,n+1):        
        c.append(x)
        if depth==m:
            print(' '.join(map(str,c)))                
        else:                
            dfs(x,depth+1)
        c.pop()            
dfs(1,1)