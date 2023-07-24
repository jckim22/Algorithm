from collections import deque
t=int(input())
con=[deque(map(int,input())) for _ in range(t)]
k=int(input())
case=[list(map(int,input().split())) for _ in range(k)]
right=2
left=6
def Leftrot(c,l,cs):         
    if c==0:    
        return    
    nl=con[c-1][left]    
    r=con[c-1][right]
    if l==r:        
        return
    else:
        if cs>0:
            con[c-1].rotate(-1)
            Leftrot(c-1,nl,-1)
        else:
            con[c-1].rotate(1)
            Leftrot(c-1,nl,1)
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
    con[cas[0]-1].rotate(cas[1])
    Leftrot(cas[0]-1,nl,cas[1])
    Rightrot(cas[0]-1,nr,cas[1])
result=0
for x in con:
    if x[0] == 1:
        result+=1
print(result)
        
        
    
    