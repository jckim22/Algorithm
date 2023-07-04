N = int(input())
V = list(input().split())

# 동 북 서 남
dx = [0, -1, 0, 1] #세로축 행
dy = [1, 0, -1, 0] #가로축 열

move_type = ['R','U','L','D']

x,y=1,1

for i in V:
    
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx=x+dx[j]
            ny=y+dy[j]
    
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    
    x=nx
    y=ny
    
print(f'{x} {y}')


# start = [1,1]

# for x in range(len(V)):

#     if V[x] == 'R':
#         start[1] += dy[0]
#         if start[1] > N:
#             start[1] -= 1
#     elif V[x] == 'L':
#         start[1] += dy[2]
#         if start[1] < 1:
#             start[1] += 1
#     elif V[x] == 'U':
#         start[0] += dx[1]
#         if start[0] < 1:
#             start[0] += 1
            
#     elif V[x] == 'D':
#         start[0] += dx[3]
#         if start[0] > N:
#             start[0] -=1

        
    
# print(start)