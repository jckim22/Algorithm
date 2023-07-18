n,k,p,x = map(int, input().split())
led=[[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
nb=[]
nx=[]

def curLed():
    for a in str(n):
        nb.append(a)
    for a in str(x):
        nx.append(a)
    curled=0
    cur=[]
    for a in range(k-len(nx)):
        for ledc in led[0]:
            cur.append(ledc)
    for a in nx:
        a=int(a)    
        for ledc in led[a]:
            cur.append(ledc)
    return cur
cur=curLed()
def changeLed(i):
    ni=[]
    for a in str(i):
        ni.append(a)
    curled=0
    cLed=[]
    for a in range(k-len(ni)):
        for ledc in led[0]:
            cLed.append(ledc)
    for a in ni:
        a=int(a)    
        for ledc in led[a]:
            cLed.append(ledc)
    return cLed


def compLed(i,j):
    cnt=0
    for o in range(len(i)):
        if i[o]!=j[o]:
            cnt+=1
    return cnt

result=0
for i in range(1,n+1):
    cLed=changeLed(i)
    if p>=compLed(cur,cLed):
        result+=1
    
print(result-1)
    
            