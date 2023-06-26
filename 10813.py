n,m=map(int,input().split())
v=list()
for x in range(0,n):
    v.append(x+1)
for x in range(0,m):
    a,b=map(int,input().split())
    v[a-1],v[b-1]=v[b-1],v[a-1]
    
for x in v:
    print(x,end=' ')   