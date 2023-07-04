v = input()

x = int(v[1])
y = ord(v[0])-96
cnt = 0

# # 동서남북 방향벡터
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# move_type = ['R','L','S','N']
# moving = [
# ['R','R','S'],
# ['R','R','N'],
# ['L','L','S'],
# ['L','L','N'],
# ['N','N','R'],
# ['S','S','L'],
# ['N','N','L'],
# ['S','S','R']
# ]

# for moves in moving:
#     nx = x
#     ny = y
#     for move in moves:
#         for i in range(len(move_type)):
#             if move == move_type[i]:
#                 nx+=dx[i] 
#                 ny+=dy[i]
            
#     if nx > 8 or ny > 8 or nx < 1 or ny < 1:
#         continue
#     cnt +=1
    
    
# print(cnt)
            
            

movings = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

for moving in movings:
    nx = x
    ny = y
    
    nx += moving[0]
    ny += moving[1]
    
    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue
    cnt +=1
    
print(cnt)