#아이디어
#먼저 0인 좌표들을 전부 다 찾는다.abs
#0인 좌표들마다 1~9까지 대입해보며 넣을 수 있는지 확인한다.abs
#만약 안될 떄는 결국 원인인 부분까지 올라가서 다른 수를 대입하며 반복하게 될 것이다.abs
#세로 확인 -> 그 열에 넣으려고 하는 수가 있는지 찾는다
#가로 확인 -> 그 행에 넣으려고 하는 수가 있는지 찾는다
#3x3칸 확인 -> 해당 좌표 x,y를 각각 3으로 나누고 3을 곱하면 3의 배수로 해당하는 좌표에 시작점이 될 것이다.abs
#-> for문으로 nx+x ,ny+y로 돌며 넣으려고 하는 수가 있는지 확인한다.abs
#모든 빈칸은 채우면 출력
from sys import stdin
input=stdin.readline
sudoku=[list(map(int,input().split())) for _ in range(9)]
zero=[]
for x in range(9):
    for y in range(9):
        if sudoku[x][y]==0:
            zero.append([x,y])
end_depth=len(zero)
def check(x,y,target):    
    #가로 확인
    for i in range(9):
        if sudoku[x][i]==target:
            return False
    #세로 확인
    for i in range(9):
        if sudoku[i][y]==target:
            return False        
    #3x3 사각형 확인        
    nx=x//3*3
    ny=y//3*3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == target:
                return False    
    return True
            
def dfs(depth,idx):
    if depth==end_depth:
        for y in range(9):
            print(*sudoku[y])
        exit()
    r=zero[idx][0]
    c=zero[idx][1]
    for x in range(1,10):        
        if check(r,c,x):
            sudoku[r][c]=x
            dfs(depth+1,idx+1)
            sudoku[r][c]=0
dfs(0,0)