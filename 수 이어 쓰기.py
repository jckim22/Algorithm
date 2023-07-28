s=input()
sidx=0
answer=1
check=False
while True:
    sanswer=str(answer)
    for x in sanswer:
        if s[sidx]==x:
            sidx+=1
            if sidx==len(s):
                check=True
                break
    if check:
        break
    answer+=1

print(answer)
    
    
    
        