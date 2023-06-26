def solution(k, tangerine):
    cnt = dict()
    answer=0
    for v in tangerine:
        try: cnt[v] += 1
        except: cnt[v] = 1
        
    print(cnt)
    while(True):
        mx=max(cnt,key=cnt.get)
        if(cnt[mx]>=k):
            answer+=1
            break
        elif(cnt[mx]<k):
            answer+=1
            k-=mx
            del cnt[mx]
    
    return answer

k=4
tangerine=[1, 3, 2, 5, 4, 5, 2, 3]
solution(k, tangerine)
