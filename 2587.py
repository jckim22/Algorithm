from sys import stdin

number=list()
cnt=0
while cnt<5:
    number.append(int(stdin.readline()))
    cnt+=1
    
number.sort()

print(int(sum(number) / len(number)))
print(number[2])


    