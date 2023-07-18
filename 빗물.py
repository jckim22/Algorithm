row,col = map(int,input().split())
world=[[0 for _ in range(col)] for _ in range(row)]
tmp1=list(map(int,input().split()))
for x in range(col):
    tmp=tmp1[x]
    for y in range(tmp):
        world[y][x]=1
blockOn=False     
cnt=0       
result=0    
for x in range(row):
    cnt=0
    blockOn=False
    for y in range(col):
        if blockOn and world[x][y]==0:
            cnt+=1
        if world[x][y]==1:
            blockOn=True
            result+=cnt
            cnt=0
print(result)            