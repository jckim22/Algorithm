from itertools import combinations

n,m = map(int,input().split())
stage=[list(map(int,input().split())) for _ in range(n)]

chicken=[]
home=[]
result=9999999
#치킨집을 선택하기 위해 치킨집과 치킨거리를 구하기 위해 집 리스트를 초기화
for x in range(n):
    for y in range(n):
        if stage[x][y]==1:
            home.append([x,y])
        elif stage[x][y]==2:
            chicken.append([x,y])
#치킨집 m개 만큼을 선택
for chi in combinations(chicken,m):
    tmp=0
    #선택 받은 치킨집으로 치킨 거리구하기
    for h in home:
        distance=99999
        for x in range(m):
            distance = min(distance,abs(h[0] - chi[x][0]) + abs(h[1] - chi[x][1]))
        tmp+=distance
    #가장 작은 치킨거리를 갖고 있는 선택의 결과가 result가 됨
    result=min(result,tmp)
    
print(result)
        