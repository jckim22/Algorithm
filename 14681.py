from sys import stdin
x,y=int(stdin.readline()),int(stdin.readline())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
if x < 0:
    if y > 0:
        print(2)
    else:
        print(3)