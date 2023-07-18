#kakao

#풀이
#1.cur <- 문자열의 길이의 반
#2.range(2,cur+1)
#3 처음부터 2개씩, 3개씩, 4개씩, 5개씩, 6개씩 ..... 비교 그 후 4개씩 나눴을 때 겹치는게 1개, 3개, 5개라면 문자열 길이는 4 + (4+1) + (4+1) = 14
from sys import stdin

s = stdin.readline()
cur=len(s)//2
cnt=0
len=len(s)

for x in range(2,cur+1):
    for y in range(0,len,x):
        if s[y:y+x] == s[y+x:y+x+x]:
            len-=x
    print(len)

            
            

