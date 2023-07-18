n=int(input())
cur=list(map(int,input()))
target=list(map(int,input()))

def solve(c,t):
    cnt=0
    for x in range(1,n):
        ##직전이 같다면 컨티뉴
        if c[x-1]==t[x-1]:
            continue
        cnt+=1
        #반전 시키기
        for y in range(x-1,x+2):
            if y<n:            
                c[y]=1-c[y]
    if c==t:
        return cnt
    else:
        return 1e9 
    
res = solve(cur[:], target)
# 첫번째 전구의 스위치를 누르는 경우
cur[0] = 1 - cur[0]
cur[1] = 1 - cur[1]
#비교
res = min(res, solve(cur[:], target) + 1)# min(첫번째 전구x, 첫번째 전구 o)
if res != 1e9:
    print(res)
else:
    print(-1)


    