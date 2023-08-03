#아이디어
#가로 줄 기준 일단 0의 위치와 들어가지 않은 수들을 구한다.
row=[[] for _ in range(9)]
sudoku=[]
need_num=[]
for x in range(9):    
    a=list(map(int,input().split()))
    for y in range(len(a)):
        if a[y]==0:
            row[x].append(y)
    sudoku.append(a)
check=[1,2,3,4,5,6,7,8,9]
ch=False
for x in range(9):
    for y in range(9):
        if sudoku[x][y]!=0:
            check.remove(sudoku[x][y])
    need_num.append(check)
    check=[1,2,3,4,5,6,7,8,9]            
def checking_sudoku():
    a=set()
    check=True
    for y in range(9):
        for x in range(9):
            a.add(sudoku[x][y])
        if sum(a)!=45:
            check=False
            return check
    a=set()
    for x in range(0,9):
        for y in range(x,x+3):
            for z in range(x,x+3):
                a.add(sudoku[y][z])
            if sum(a)!=45:
                check=False
                return check
        
        
def dfs(depth):
    if depth == 9 and checking_sudoku:
        print(sudoku)
        exit()
    
    
    

            
print(sudoku)
print(row)
print(need_num)