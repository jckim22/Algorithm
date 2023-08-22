# from sys import stdin
# n,m=map(int,stdin.readline().split())
# memo=set()
# for _ in range(n):
#     a=stdin.readline()
#     a=a.replace('\n','')
#     memo.add(a)
# keywords=set()
# m_len=len(memo)
# for _ in range(m):
#     answer=set()
#     a=stdin.readline().split(',')
#     for x in a:
#         x=x.replace('\n','')
#         keywords.add(x)
#     answer=memo-keywords
#     print(len(answer))

from sys import stdin
n,m=map(int,stdin.readline().split())
keywords=dict()
answer=n
for _ in range(n):
    keywords[stdin.readline().rstrip()]=True            
for x in range(m):
    write=list(stdin.readline().rstrip().split(',' ))    
    for y in write:
        #모든 key()들 중 y 하나
        if y in keywords.keys():
            if keywords[y]:
                keywords[y]=False
                answer-=1
    print(answer)
        

