from itertools import combinations

n,m = map(int,input().split())
stage=[list(map(int,input().split())) for _ in range(n)]

chicken=[]
home=[]
result=9999999
for x in range(n):
    for y in range(n):
        if stage[x][y]==1:
            home.append([x,y])
        elif stage[x][y]==2:
            chicken.append([x,y])

for chi in combinations(chicken,m):
    tmp=0
    for h in home:
        distance=99999
        for x in range(m):
            distance = min(distance,abs(h[0] - chi[x][0]) + abs(h[1] - chi[x][1]))
        tmp+=distance
    result=min(result,tmp)
    
print(result)
        