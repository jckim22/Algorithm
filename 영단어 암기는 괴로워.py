from sys import stdin
from collections import defaultdict
n,m=map(int,stdin.readline().split())
word=[stdin.readline().rstrip() for _ in range(n)]
words=defaultdict(int)
for x in word:    
    if len(x)>=m:        
        words[x]+=1
words=sorted(words.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for x in words:        
    print(x[0])


                

