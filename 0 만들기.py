Te=int(input())
ch=list()
# import sys
# sys.setrecursionlimit(100000)
def divide(now,res):
    if now>n:        
        tmp=res.replace(' ','')
        if eval(tmp)==0:
            print(res)
        return
    divide(now+1,res+' '+str(now))
    divide(now+1,res+'+'+str(now))
    divide(now+1,res+'-'+str(now))
    

for _ in range(Te):
    n=int(input())
    res='1'
    now=1
    divide(2,res)    
    print()



# arr=[0 for _ in range(1000001)]
    
# def divide(s,k,cnt,depth):
    
#     if depth==n-1 and s==0:
#         print(s,k,cnt,depth)
#         print('ok')
#         return
#     if cnt>n:        
#         return
#     if k=='+':
#         divide(s+cnt,'+',cnt+1,depth+1)
#         divide(s-cnt,'-',cnt+1,depth+1)
#         divide(s*10+cnt,'/',cnt+1,depth+1)
#     elif k=='-':
#         divide(s+cnt,'+',cnt+1,depth+1)
#         divide(s-cnt,'-',cnt+1,depth+1)
#         divide(s*10+cnt,'/',cnt+1,depth+1)
#     else:
#         divide(s+cnt,'+',cnt+1,depth+1)
#         divide(s-cnt,'-',cnt+1,depth+1)
#         divide(s*10+cnt,'/',cnt+1,depth+1)
# divide(1,'+',2,0)
# divide(1,'-',2,0)
# divide(1,'/',2,0)