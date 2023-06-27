n = int(input())
m = list(map(int,input().split()))

m = sorted(m)
cnt=0
result = 0

for x in range(len(m)):
    cnt+=1
    if cnt>=m[x]:
        result+=1
        cnt=0
        
print(result)
        
