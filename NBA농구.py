n = int(input())
t = [list(input().split()) for _ in range(n) ]

asco=0
bsco=0
idx=0
acnt=0
bcnt=0
for x in range(48):
    for y in range(60):
        if x<10:    
            m='0'+str(x)
        else:
            m=str(x)

        if y<10:
            s='0'+str(y)
        else:
            s=str(y)
            
        try:
            if t[idx][1]==f'{m}:{s}' and idx<n:        
                if t[idx][0] == '1':
                    asco+=1
                else:
                    bsco+=1                    
                idx+=1
        except:
            pass
        if asco>bsco:
            acnt+=1
            
        elif asco==bsco:
            continue
        else:
            bcnt+=1
        

am=str(acnt//60)
asc=str(acnt%60)

bm=str(bcnt//60)
bsc=str(bcnt%60)
            
if acnt//48<10:
    am='0'+am
if acnt%60<10:
    asc='0'+asc
if bcnt//48<10:
    bm='0'+bm
if bcnt%60<10:
    bsc='0'+bsc
    
print(f'{am}:{asc}')
print(f'{bm}:{bsc}')
    
            
            
        