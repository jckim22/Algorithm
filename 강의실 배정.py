from sys import stdin
import heapq

n = int(stdin.readline())

s=[]

for x in range(n):
    a = list(map(int,stdin.readline().split()))
    s.append(a)

s=sorted(s,key=lambda x:x[0])

r = []
heapq.heappush(r,s[0][1]) #첫번째 강의의 끝나는 시간을 큐에 push

for x in range(1,len(s)): #두번째 강의부터 비교
    if s[x][0] < r[0]: #만약 반복문의 비교하는 강의의 시작시간이 현재 큐의 첫번째 강의실 종료시간보다 작다면
        heapq.heappush(r,s[x][1]) #강의실 개설
    else:              #현재 큐의 첫번째 강의실에서 이어서 강의 가능함
        heapq.heappop(r) #큐는 그저 강의실 개수를 측정하기 위함이므로 한 강의실에서 다음 강의가 이어진다면 다음 강의를 pop해준다
        heapq.heappush(r,s[x][1]) #이어지는 강의 푸쉬 다음 반복부터는 다른 강의실 비교 시작
        
print(len(r))
        

#O(n2) 풀이

# cnt=0 

# s=sorted(s,key=lambda x:(x[1],x[0]))


# cur=s[0][1]

# del s[0]

# while len(s)>0:
#     check=True
    
#     for i in range(len(s)):
#         if s[i][0]>=cur:
#             cur=s[i][1]
#             check=False
#             del s[i]
#             break
#     if not check:
#         continue
#     elif check:
#         cnt+=1
#         cur=s[0][1]
#         del s[0]
        

# cnt+=1

# print(cnt)
        
        
