# t=int(input())    
# for x in range(t):
#     s=input()
#     k=int(input())
    # shortans=99999
    # longans=-1
    # anschk=False
    # check=False  
    # for y in range(len(s)):
    #     cnt=0
    #     scnt=0
    #     for z in range(y,len(s)):    
    #         cnt+=1
    #         if s[y]==s[z]:
    #             scnt+=1
    #         if scnt==k:
    #             check=True
    #             anschk=True
    #             break
    #     if check:
    #         shortans=min(shortans,cnt)
    #         longans=max(longans,cnt)
    #         check=False
    # check=False
    # if not anschk:
    #     print(-1)        
    # else:
    #     print(shortans,end=' ')
    #     print(longans)
    
from collections import defaultdict
            
t=int(input())    
for x in range(t):
    s=input()
    k=int(input())
    alpha=defaultdict(list)
    for y in range(len(s)):
        if s.count(s[y])>=k:
            alpha[s[y]].append(y)
    if not alpha:
        print(-1)
        continue        
    minans=999999
    maxans=0
    for y in alpha.values():
        for z in range(len(y)-k+1):
            minans=min(y[z+k-1]-y[z]+1,minans)
            maxans=max(y[z+k-1]-y[z]+1,maxans)            
    print(minans,maxans)
    