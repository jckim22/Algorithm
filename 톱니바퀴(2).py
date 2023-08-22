from collections import deque
t=int(input())
con=[deque(map(int,input())) for _ in range(t)]
k=int(input())
case=[list(map(int,input().split())) for _ in range(k)]
right=2
left=6
#왼쪽방향 회전
def Leftrot(c,l,cs):      
    #왼쪽 끝이면 리턴   
    if c==0:    
        return    
    #회전하기 전 9시방향 극을 담아놓음
    nl=con[c-1][left]    
    #회전하기 전 3시방향 극을 담아놓음
    r=con[c-1][right]
    #이전 톱니바퀴의 9시방향과 현재 톱니바퀴의 3시방향의 극이 같다면 리턴
    if l==r:        
        return
    #아니라면 회전 후 다음 톱니바퀴로 들어감
    else:
        if cs>0:
            con[c-1].rotate(-1)
            Leftrot(c-1,nl,-1)
        else:
            con[c-1].rotate(1)
            Leftrot(c-1,nl,1)
#오른쪽방향 회전            
def Rightrot(c,r,cs):         
    if c==t-1:        
        return
    nr=con[c+1][right]    
    l=con[c+1][left]
    if r==l:        
        return
    else:
        if cs>0:
            con[c+1].rotate(-1)
            Rightrot(c+1,nr,-1)
        else:
            con[c+1].rotate(1)
            Rightrot(c+1,nr,1)            
for cas in case:
    nr=con[cas[0]-1][right]
    nl=con[cas[0]-1][left]      
    #해당 톱니바퀴 회전
    con[cas[0]-1].rotate(cas[1])
    Leftrot(cas[0]-1,nl,cas[1])
    Rightrot(cas[0]-1,nr,cas[1])    
#결과    
result=0
for x in con:
    if x[0] == 1:
        result+=1
print(result)
        
        
    
    