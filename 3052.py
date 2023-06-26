a=list()

for x in range(0,10):
    a.append(int(input())%42)
a=set(a)
print(len(a))
