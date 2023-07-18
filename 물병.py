# n,k=map(int,input().split())
# check = 0b000000000
# cnt=0


# while N>K:
#     if N%2==1:
#         check |= (1<<cnt)
#         N+=1
#     N/=2
#     print(cnt,check)
#     cnt+=1
# print(check)
    
import sys

n, k = map(int, input().split())

count = 0;

while bin(n).count('1') > k:
    n +=1
    count +=1
print(count)    

# while(True):
    



cnt=0
A=1

while(N>K):
    R=N%2
    cnt+=R*A
    A*=2
    N//=2
    N+=R

print(cnt)