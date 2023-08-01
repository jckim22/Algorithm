#아이디어
#일단 해당 행의 0~n-1의 열로 반복문을 돌릴 것이다.
#1. 먼저 0행에 0열에 퀸을 놓을 수 있는지 확인 넣을 수 있다면
#2. 1행으로 재귀해 0열확인 안되니까 1열도확인 하면서 된다면 또 2행으로 재귀
#3. 이렇게 하여 n행까지 도달하게 되면 answer+1
#4. 그 다음 이제 0행의 1열에 퀸을 놓을 수 있는지 확인 이후 1행의 0열부터 다시 가능한지 확인한다.
#5. 이 과정을 반복 결국 가장 큰 반복은 0행의 0열부터 n-1열까지이고 그 밑 행은 0행의 열이 정해진 뒤로 또 차례로 정해진다.abs
#6. 이 문제에서는 in으로 탐색하는 것이 아니고 1차원 배열을 초기화하며 확인하는 것이기 때문에 pop이나 remove가 필요없는 백트랙킹이다.abs
#시간복잡도
#1 0행부터 n행까지 반복하면서 일단 n
#2 확인하는 과정에서 n에 가까이 소요됨 n^2
#3 가능한 열을 찾는 과정에서 또 n정도 소요됨 n^3
#4 한번 수행하는데는 약 3,375번에 연산을 수행하지만 이 과정을 무수히 수행하기에 시간이 많이 소요될 것이다.
#5 보통 중복이 없는 백트랙킹은 O(n!) 정도로 보는데 15!은 대충 1천억 정도 된다.
#6 이 문제에서 주어진 시간은 10초지만 파이썬 한정으로 더 많이 줄 것이다.abs
#7 파이썬으로는 풀 수 없을 것 같고 pypy로 간당간당하게 합격할 수도 있을 것 같다.
#자료구조
#1차원 리스트:row

from sys import stdin
input=stdin.readline                
n=int(input())
answer=0
row=[0] * n
def queen_check(r):
    for x in range(r):
        #열이 같은지,행이 같은지, 대각선인지
        if row[r]==row[x] or abs(row[r]-row[x])==abs(r-x):
            #해당된다면 그곳에 놓을 수 없다.
            return False
    return True

def dfs(r):
    global answer,n
    #다 도달한 것임으로 이제 그만
    if r==n:
        answer+=1
        return
    else:
        #n열까지 탐색
        for x in range(n):
            #r번째 row의 x열에 퀸을 놓을 수 있는지 탐색하겠다.
            row[r]=x
            if queen_check(r):
                dfs(r+1)
dfs(0)
print(answer)