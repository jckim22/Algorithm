n=int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
arr = list()
for x in range(n):
    arr.append(list(input()))
cnt=1
def divide(srow,scol,n):
    global cnt
    
    cnt+=1
    
    check=True
    s=arr[srow][scol]
    # for x in range(srow,srow+n):
        # for y in range(scol,scol+n):
            # print(arr[x][y],end='')
            
        # print()
    for x in range(srow,srow+n):
        for y in range(scol,scol+n):
            if s!=arr[x][y]:
                check=False
                break
        if not check:
            break
        
    if check:
        print(s,end="")
        return
    else:
        print('(',end="")
        divide(srow,scol,n//2)
        divide(srow,scol+n//2,n//2)
        divide(srow+n//2,scol,n//2)
        divide(srow+n//2,scol+n//2,n//2)        
        print(')',end="")
    
    
divide(0,0,n)





