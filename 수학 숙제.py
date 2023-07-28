#브루트포스
#O(n2) 가능
#숫자를 담을 변수
#하나씩 담는다 문자가 나오면 리스트에 숫자를 append
#set하고 list로 만들어서 정렬
#0은 하나만 나오고 그 다음에 0이 나오면 그냥 0, 숫자가 나오면 생략

num=''
numOn=False
answer=[]
n = int(input())
s = [input() for _ in range(n)]
for x in s:
    for y in x:
        if numOn and y.isalpha():
            answer.append(int(num))
            num=''
            numOn=False
            continue
        elif not y.isalpha():                
            num+=y
            numOn=True  
    if num:
        answer.append(int(num))
        num=''
        numOn=False
answer=sorted(answer,key=lambda x:x)
for x in answer:
    print(x)
            
            
            
        