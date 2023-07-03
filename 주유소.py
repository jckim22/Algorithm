from sys import stdin

N = int(stdin.readline())
road = list(map(int,stdin.readline().split()))
cost = list(map(int,stdin.readline().split()))
mi = cost[0]
answer = 0
for x in range(N-1):
    if mi>cost[x]:
        mi = cost[x]
    answer +=  mi*road[x]
    
print(answer)
    