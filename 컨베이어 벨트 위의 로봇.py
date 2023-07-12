from collections import deque

n,k=map(int,input().split())
A=list(map(int,input().split()))
A=deque(A)
robot=deque([False]*n)
result=0

while True:
    result+=1
    #벨트와 로봇이 동시에 한칸씩 회전
    A.rotate(1)
    robot.rotate(1)
    #내리는 위치에서 로봇 삭제
    robot[-1]=False
    #내리는 위치전부터 올리는 위치까지 반복
    for x in range(n-2,-1,-1):
        #그 다음 로봇의 이동
        #로봇이 이동하려는 위치에 로봇이 없고 그 곳의 내구도가 0이 아니면 이동한다.
        if robot[x] and not robot[x+1] and A[x+1]>0:
            robot[x]=False
            robot[x+1]=True
            A[x+1]-=1
    #내리는 위치에서 로봇 삭제
    robot[-1]=False
    #올리는 위치에 내구도가 0이 아니라면 로봇을 한 개 올린다.
    if A[0]>0:
        robot[0]=True
        A[0]-=1
    #내구도 0이 k개 이상이면 종료
    if A.count(0)>=k:
        break
    
print(result)
    
    
        
    
        
        
            







# A=[]
# for x in range(len(tmp)):
#     t=[tmp[x],False]
#     A.append(t)
# zero=0
# cnt=0
# robot=0
# A=deque(A)
# while zero<k:
#     robot+=1
#     if robot>n:
#         robot-=1
#     for z in range(2*n-1,2*n-robot-1,-1):
#         if A[z][0]>0 and A[z-1][0]>0:
#             A[z][0]-=1                
#     for y in range(len(A)):
#         if A[y][0]==0 and not A[y][1]:
#             zero+=1
#             A[y][1]=True
#     print(A)
#     print(cnt)
#     belt=A.popleft()
#     A.append(belt)
#     cnt+=1
#     print(A)
#     print(cnt)
        
        
# print(cnt)


        