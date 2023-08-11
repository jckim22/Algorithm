from sys import stdin
from collections import defaultdict
input=stdin.readline
n,m=map(int,input().split())
s=set()
for _ in range(n):
    s.add(input().strip())
cnt=0
for x in range(m):
    tmp=input().strip()
    if tmp in s:
        cnt+=1
print(cnt)
