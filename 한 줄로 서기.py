n = int(input())
s = list(map(int,input().split()))
arr = []

cnt=0

for x in range(0,n): #주어진 배열과 정해진 키로 이루어진 이차원 리스트 초기화
    l=[s[x],x+1]
    arr.append(l)

arr=sorted(arr,key=lambda x:x[1],reverse=True)

while True:
    check=True
    for x in range(n):
        cnt=0
        for y in range(x):
            if arr[y][1]>arr[x][1]:
                cnt+=1
        if arr[x][0] > cnt:
            arr[x],arr[x+1] = arr[x+1],arr[x]
            check=False
        elif arr[x][0] < cnt:
            arr[x],arr[x-1] = arr[x-1],arr[x]
            check=False
    if check:
        break
    
for x in range(n):
    print(arr[x][1],end=' ')

        

