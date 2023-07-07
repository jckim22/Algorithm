pwd=input()
moeum = ['a','e','i','o','u']

while pwd != 'end':
    check=[False,True,True]
    mcnt=0
    zcnt=0
    for x in range(len(pwd)):
        for y in moeum:
            if pwd[x]==y:
                check[0]=True
                break
        if check[0]:
            break    
    
    for x in range(len(pwd)):
        tmpc=False
        for y in moeum:
            if pwd[x]==y:
                zcnt=0
                mcnt+=1
                tmpc=True
                break
        if not tmpc:
            zcnt+=1
            mcnt=0
        if zcnt>2 or mcnt>2:
            check[1]=False
            break
    
    for x in range(len(pwd)-1):
        if len(pwd)<=1:
            break
        if pwd[x]==pwd[x+1] and pwd[x]!='e' and pwd[x]!='o':
            check[2]=False
    
    if check[0] and check[1] and check[2]:
        print(f"<{pwd}> is acceptable.")
    else:
        print(f"<{pwd}> is not acceptable.")
            
    pwd=input()
    