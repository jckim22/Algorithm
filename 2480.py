a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b!=c or a==c!=b or b==c!=a:
    if a==b or a==c:
        print(1000+a*100)
    else:
        print(1000+b*100)
else:
    num=list(map(int,[a,b,c]))
    print(max(num)*100)

        