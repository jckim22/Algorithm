# t=int(input())    
# for x in range(t):
#     s=input()
#     k=int(input())
#     shortans=99999
#     longans=-1
#     anschk=False
#     check=False  
#     for y in range(len(s)):
#         cnt=0
#         scnt=0
#         for z in range(y,len(s)):    
#             cnt+=1
#             if s[y]==s[z]:
#                 scnt+=1
#             if scnt==k:
#                 check=True
#                 anschk=True
#                 break
#         if check:
#             shortans=min(shortans,cnt)
#             longans=max(longans,cnt)
#             check=False
#     check=False
#     if not anschk:
#         print(-1)        
#     else:
#         print(shortans,end=' ')
#         print(longans)
    
# dict에 key 값이 없어도 원하는 값을 append 할 수 있음
from collections import defaultdict            
t=int(input())    
for x in range(t):
    s=input()
    k=int(input())  
    alpha=defaultdict(list)
    #문자가 k개 이상인 문자들을 key로 하고 그에 맞는 인덱스번호를 value로 append
    for y in range(len(s)):
        if s.count(s[y])>=k:
            alpha[s[y]].append(y)
    #k개가 되는 문자가 없다면 -1
    if not alpha:
        print(-1)
        continue        
    minans=999999
    maxans=0
    #딕셔너리의 value인 리스트를 대상으로 문자열 게임 시작
    for y in alpha.values():
        #문자개수를 k에 맞춰서 끝에서 처음을 빼는 방식으로 길이 계산 후 최소와 최대 길이를 구함
        for z in range(len(y)-k+1):
            minans=min(y[z+k-1]-y[z]+1,minans)
            maxans=max(y[z+k-1]-y[z]+1,maxans)            
    print(minans,maxans)
    