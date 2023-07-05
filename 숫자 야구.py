from sys import stdin

N=int(stdin.readline())
cur=[]
for x in range(100,1000):
    strx=str(x)
    if strx[0]!=strx[1] and strx[1]!=strx[2] and strx[0] != strx[2]:
        if strx[0]!='0' and strx[1] !='0' and strx[2] !='0':
            cur.append(x)
answer=[]

for x in range(N):
    num,s,b = map(int,stdin.readline().split())
    str_num=str(num)
    for bf_num in cur:
        str_bf_num=str(bf_num)
        tmps=0
        tmpb=0
        for y in range(3):
            for z in range(3):
                if str_num[y] == str_bf_num[z]:
                    if y==z:
                        tmps+=1
                        break
                    tmpb+=1
        if tmps == s and tmpb == b:
            answer.append(bf_num)        
    cur = answer
    answer=[] 
        
print(len(cur))



            
    

