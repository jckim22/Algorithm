k,s,n=input().split()
n=int(n)
case=[input() for _ in range(n)]
#방향벡터 설정
move=['R','L','B','T','RT','LT','RB','LB']
dr=[0,0,-1,1,1,1,-1,-1]
dc=[1,-1,0,0,1,-1,1,-1]
king=[]
stone=[]
#킹과 돌의 위치를 숫자 인덱스 좌표로 변경
for x in k:
    if x.isalpha():
        king.append(ord(x)-65)
        continue
    king.append(int(x)-1)
for x in s:
    if x.isalpha():
        stone.append(ord(x)-65)
        continue
    stone.append(int(x)-1)
#row와 col에 순서에 맞게 스왑
king[0],king[1]=king[1],king[0]
stone[0],stone[1]=stone[1],stone[0]
for cs in case:
    for x in range(len(move)):
        #킹의 현재위치 (이동용)
        nr=king[0]
        nc=king[1]
        #돌의 현재위치 (이동용)
        nrs=stone[0]
        ncs=stone[1]
        #킹의 현재위치 (되돌리기용)
        nrh=king[0]
        nch=king[1]
        #방향이동
        if cs == move[x]:
            nr+=dr[x]
            nc+=dc[x]
            if nr<0 or nr>7 or nc<0 or nc>7:
                continue
            king[0]=nr
            king[1]=nc
            if king[0]==stone[0] and king[1]==stone[1]:
                nrs+=dr[x]
                ncs+=dc[x]
                if nrs<0 or nrs>7 or ncs<0 or ncs>7:
                    king[0]=nrh
                    king[1]=nch
                    continue
                stone[0]=nrs
                stone[1]=ncs
#정답으로 변환        
k=''
s=''                
k+=chr(king[1]+65)
k+=str(king[0]+1)
s+=chr(stone[1]+65)
s+=str(stone[0]+1)
print(k)
print(s)
            
