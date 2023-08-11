#아이디어 
#R과 D, 두 개의 함수밖에 존재하지 않으므로 함수에 따라 MODE를 변경해서 왼쪽으로 pop할지 오른쪽에서 pop할지를 결정한다.
#만약 큐기 비면 error를 출력
#시간 복잡도
#reverse로 배열을 거꾸로 돌리지 않고 사용하는 건 pop 밖에 없으니 충분히 가능하다고 보임
#총 O(n)의 수행시간

from collections import deque
from sys import stdin
input=stdin.readline
t=int(input())
#O(100)
for _ in range(t):
    mode=True
    check=True
    func=input().strip()
    n=int(input())
    arr=input().strip()
    arr=arr.replace('[','')
    arr=arr.replace(']','')
    if arr:
        arr=deque(list(map(int,arr.split(','))))
    #O(n)
    elif not arr and 'D' not in func:
        print('[]')
        continue
    else:
        print('error')
        continue
    #O(n)
    for x in func:
        if x == 'R':
            mode=not mode
        elif x == 'D':            
            if mode:
                if arr:
                    arr.popleft()                
                else:
                    check=False
                    print('error')
                    break
            else:
                if arr:
                    arr.pop()                
                else:
                    check=False
                    print('error')
                    break
    if not check:
        continue
    if not arr:
        print('[]')
        continue
    answer='['
    #O(n)
    if mode:
        for x in arr:
            answer+=str(x)+','
    else:
        for x in range(len(arr)-1,-1,-1):      
            answer+=str(arr[x])+','
    answer=answer[:-1]
    answer+=']'
    print(answer)
