#첫 풀이
from collections import defaultdict,deque
n=int(input())
srr=[input() for _ in range(n)]
cnt=0
#알파벳 딕셔너리 생성
alpha=defaultdict(list)
for x in range(97,122):
    alpha[chr(x)].append(0)

q=deque(srr)
maxlen=0
#최장 길이를 구함
for x in range(n):
    maxlen=max(len(srr[x]),maxlen)
cnt=0
tmp=[]
#최장 길이만큼 반복
for y in range(maxlen):
    check=0 
    #큐의 크기(단계를 거쳐낸 문자열들)만큼 반복 진행
    while q:
        s=q.popleft()
        #해당 번째 알파벳에 같은 것이 있으면 append
        for x in range(97,122):
            if len(s)>cnt:
                if s[cnt]==chr(x):
                    alpha[chr(x)].append(s)
    #알파벳중 밸류가 2보다 큰 것(0과 문자열 2개)은 단계를 통과한 것이므로
    for z in alpha.values():
        if len(z)>2:
            #check
            check+=1
    #check가 없다면 단계 통과 실패니까 break            
    if check==0:        
        break
    #이번 단계도 실패하지 않았다면 한번 더 측정을 위해 tmp를 초기화
    tmp=[]             
    #단계를 통과한 문자열들을 q에 append함
    for z in alpha.values():
        if len(z)>2:            
            tmp.append(z)
            for i in z:
                if i !=0:
                    q.append(i)
    #alpha 딕셔너리도 초기화
    alpha=defaultdict(list)
    for x in range(97,122):
        alpha[chr(x)].append(0)
    #다음번째 문자를 검사하기 위해 cnt를 +1해준다                    
    cnt+=1    
print(tmp)
if not tmp:
    print(srr[0])
    print(srr[1])
else:
    print(tmp[len(tmp)-1][1])
    print(tmp[len(tmp)-1][2])




n=int(input())
srr=[input() for _ in range(n)]
for x in enumerate(srr):
    srr[x[0]]=x
def check(x,y):
    cnt=0
    min_len=min(len(x),len(y))    
    for i in range(min_len):
        if x[i]==y[i]:
            cnt+=1
        else:
            return cnt
    return cnt
maxlen=[-1,-1,0]        
for x in range(n):
    for y in range(x+1,n):    
        cur=check(srr[x][1],srr[y][1])            
        if maxlen[2] < cur:
            maxlen[0]=x
            maxlen[1]=y
            maxlen[2]=cur          
print(srr[maxlen[0]][1])
print(srr[maxlen[1]][1])


n = int(input())
a = [input() for _ in range(n)]

# n = 9
# a = ["noon", "is", "for","lunch","most","noone","waits","until","two"]

# 입력받은 문자들을 인덱스와 함께 사전순으로 정렬한다.
b = sorted(list(enumerate(a)),key = lambda x: x[1])
# b = [(2, 'for'), (1, 'is'), (3, 'lunch'), (4, 'most'), (0, 'noon'), (5, 'noone'), (8, 'two'), (7, 'until'), (6, 'waits')]

# check 함수는 글자 하나하나가 서로 같은지 탐색
def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]: cnt += 1
        else: break
    return cnt

# 최장 접두사를 가진 문자열 담아둘 리스트 생성
length = [0] * (n+1)
maxlength = 0

for i in range(n-1):
    # 인접한 두개의 문자열을  check함수에 대입
    # tmp 값은 동일한 접두사의 길이
    tmp = check(b[i][1], b[i+1][1])
    # 최장 접두사 길이 갱신
    maxlength = max(maxlength, tmp)
    
    # b[i][0]은 문자가 입력된 순서, 즉 인덱스
    # length 에 입력된 순서에 자기 접두사 길이를 저장
    # max 함수로 이전 값하고 현재 값하고 비교하여 집어넣음
    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i+1][0]] = max(length[b[i+1][0]], tmp)
    # length = [4, 0, 0, 0, 0, 4, 0, 0, 0, 0]
    
first = 0
for i in range(n):
    # 입력된 순서대로 접두사의 길이 비교
    if first == 0:
        # 만약 현재 접두사의 길이가 최장접두사라면
        if length[i] == max(length):
            # 제일 먼저 입력된 문자 출력
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else:
    	# 다음으로 입력되었된 값들 중 최장 접두사 출력후 종료
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break


        
        

        
        
