arr=[[0 for x in range(8)] for y in range(16)]

q = list(input().split())


cnt = 0

for x in range(16):
    try:
        if arr[x].count(0) == 0:
            continue
        
        elif q[cnt] == 'long':
            if arr[x].count(0) != 8:
                for z in range(8):
                    arr[x+1][z]=4
                for z in range(8):
                    arr[x+2][z]=4

            elif arr[x].count(0) == 8:
                for z in range(8):
                    arr[x][z]=4
                for z in range(8):
                    arr[x+1][z]=4
            cnt+=1
        elif q[cnt] == 'int':
            if arr[x].count(0) != 8:
                for z in range(8):
                    arr[x+1][z]=3
            elif arr[x].count(0) == 8:
                for z in range(8):
                    arr[x][z]=4
            cnt+=1
    except:
        break
    
print(arr)
    
                
        
        
