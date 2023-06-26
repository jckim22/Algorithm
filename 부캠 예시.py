arr = list(map(int,input().split()))
arr.sort()
answer = list()
answers = list()
cnt = 0
tf = True

# for x in range(0,len(arr)):
#     cnt+=1

#     if arr[x] < arr[x+1]:
#         answer.append(cnt)
#         cnt = 0
    
#     if x == len(arr)-2:
#         cnt+=1
#         answer.append(cnt)
#         break

# for x in answer:
#     if x > 1:
#         tf=False
#         answers.append(x)
        
# if tf:
#     print(-1)
# else:
#     print(answers)
    
    
for x in range(0,max(arr)+1):
    if arr.count(x) > 1:
        tf=False
        answers.append(arr.count(x))
        
        
if tf:
    print(-1)
else:
    print(answers)
    
    
    

