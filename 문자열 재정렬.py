s = input()
answer = []
num = 0

# s= sorted(s)
# cnt=0
# num=0
# for x in s:
    
#     if x >= 'A' and x <='z':
#         break
    
#     cnt+=1
    
# for x in range(cnt):
#     num+=int(s[x])
    
# answer = s[cnt:]
# if num != 0:
#     answer += str(num)

# # for x in answer:
# #     print(x,end='')

# print(''.join(answer))

for x in s:
    if x.isalpha():
        answer.append(x)
    else:
        num+=int(x) 
        
answer = sorted(answer)

if num != 0:
    answer.append(str(num))
    
print(''.join(answer))

        

        