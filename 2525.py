from sys import stdin
a,b=map(int,stdin.readline().split())
c=int(stdin.readline())

print(a+(b+c)//60 if a+(b+c)//60<24 else a+(b+c)//60-24,(b+c)%60)
