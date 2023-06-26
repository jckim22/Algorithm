from sys import stdin

N,K = map(int,stdin.readline().split())

cnt=0

while(True):
    if N==1:
        break
    elif N % K == 0:
        N/=K
    else:
        N-=1
        
    cnt+=1
    
print(cnt)
    
    