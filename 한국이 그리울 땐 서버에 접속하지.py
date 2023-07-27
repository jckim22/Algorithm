# import re
# n=int(input())
# s=input()
# s=s.replace('*','.*')
# regex=re.compile(s)
# for x in range(n):
#     ss=input()
#     reg=regex.search(ss)    
#     if reg.group()==ss:
#         print('DA')
#     else:
#         print('NE')


# import re
# n=int(input())
# s=input()
# s=s.replace('*','.*')
# regex=re.compile(s)
# for x in range(n):
#     ss=input()    
#     if regex.fullmatch(ss):
#         print('DA')
#     else:
#         print('NE')
        
        
import re
n=int(input())        
regex=re.compile('.*'.join(input().split('*')))
for x in range(n):
    ss=input()    
    if regex.fullmatch(ss):
        print('DA')
    else:
        print('NE')
        