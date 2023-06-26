from sys import stdin
x = int(stdin.readline())
cnt = 0
while (True):
    if x % 3 == 0:
        x = x/3
        cnt += 1
        if x == 1:
            print(cnt)
        break
    elif x % 2 == 0:
        x = x/2
        cnt += 1
        if x == 1:
            print(cnt)
        break

    x = x - 1
    cnt += 1

    if x == 1:
        print(cnt)
        break
