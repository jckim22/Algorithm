#아이디어
#일단 리스트에 수들을 담고
#딕셔너리에 연산자들을 갖고 있는 개수로 초기화 한다.\
#수의 0번째 인덱스부터 출발
#갖고 있는 연산자를 반복
#해당 연산자가 0이 아니라면 식에 넣는다
#마지막 리스트에 도달했다면 계산하고 최대값과 최소값 변수에 넣어준다.
#돌아오면서 사용했던 연산자들을 +1 해준다.
#시간복잡도
#중복이 허용되지 않고 n의 개수가 10개이므로 O(n!)의 백트랙킹으로 풀만할 것 같다.
#자료구조
#dic:연산자,1차원 list:수,1차원 list:연산자 입력 

from sys import stdin
input = stdin.readline
n=int(input())
nums=list(map(int,input().split()))
oper=dict()
operator=['+','-','*','//']
idx=0
#문제에서 -10억 ~ 10억으로 범위가 나온다고 했음
maxans=-1000000000
minans=1000000000
t=list(map(int,input().split()))
#갖고 있는 연산자 딕녀러리 생성
for x in t:    
    if x>0:
        oper[operator[idx]]=x
    idx+=1
def dfs(i,st):
    global maxans,minans
    #이번에 받은 수를 지금까지 연산했던 결과와 연산자에 더해줘서 연산을 수행    
    #//연산에 경우 내림을 하기 때문에 eval로 계산하지 않고 int(tmp/nums)로 계산하기 위함
    if '//' in st:
        st=st[:-2]
        tmp=int(st)
        st=str(int(tmp/nums[i]))
    else:
        st+=str(nums[i])
        st=eval(st)
        st=str(st)
    #최대와 최소값 구함
    if i>=n-1:             
        maxans=max(maxans,int(st))
        minans=min(minans,int(st)) 
        return
    #갖고 있는 연산자를 기준으로 반복
    for x in oper.keys():
        #만약 해당 연산자가 1개 이상 남았다면
        if oper[x]>0:
            #-1해주고
            oper[x]-=1
            #지금 값에 연산자를 붙여준다.             
            st+=x           
            #그리고 dfs 수행
            dfs(i+1,st)
            #dfs가 끝나고 돌아오는 길에 썼던 연산자를 문자열에서 삭제해줌
            if x=='//':           
                st=st[:-2] 
            else:
                st=st[:-1]                                       
            #썼던 연산자의 개수도 다시 +1
            oper[x]+=1                            
dfs(0,'')    
print(maxans)   
print(minans)