from sys import stdin

N = int(stdin.readline())
S=list()
answer=1 #첫 회의 카운트

for x in range(N): # 회의 입력 받음(2차원 리스트)
    a,b=map(int,stdin.readline().split())
    l=[a,b]
    S.append(l)
    
S=sorted(S,key=lambda y:(y[1],y[0])) # 끝나는 시간을 첫번째 기준, 시작시간을 두번째 기준으로 하여 정렬

curend = S[0][1] #현재 회의의 끝나는 시간을 담음

for x in range(1,len(S)): #현재 회의를 제외하고 반복 시작

    if S[x][0]>=curend: #현재회의의 끝나는 시간보다 시작시간이 크다면
        curend=S[x][1] #그 회의의 끝나는 시간을 현재 회의의 끝나는 시간으로 변경
        answer+=1 #회의 카운트
        
print(answer)
        