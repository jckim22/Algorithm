a=input()
acnt=a.count('a')
a+=a[0:acnt-1]
bmin=a[0:acnt].count('b')

for x in range(len(a)-(acnt-1)):
    if a[x:x+acnt].count('b')<bmin:
        bmin=a[x:x+acnt].count('b')
print(bmin)
        
        
    