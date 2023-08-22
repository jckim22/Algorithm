#브루트포스
#O(n2) 가능
num=''
numOn=False
answer=[]
n = int(input())
s = [input() for _ in range(n)]
#O(n^2)
for x in s:
    for y in x:
        #알파벳이고 임시 숫자에 넣고 있던 중이면 모아놓은 숫자를 append
        if numOn and y.isalpha():
            answer.append(int(num))
            num=''
            numOn=False
            continue
        #알파벳이 아니면 임시 변수에 넣음
        elif not y.isalpha():                
            num+=y
            numOn=True
    #숫자로 끝나서 못한 append를 해줌
    if num:
        answer.append(int(num))
        num=''
        numOn=False
#정렬        
answer=sorted(answer,key=lambda x:x)
for x in answer:
    print(x)
            
            
            
        