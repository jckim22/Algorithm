S = input()

cur =int(S[0])
for x in range(len(S)-1):
    if S[x]=='0' or S[x+1]=='0':
        cur+=int(S[x+1])
    elif S[x]=='1' or S[x+1]=='1':
        cur+=int(S[x+1])
    else:
        cur*=int(S[x+1])
        
print(cur)
        