

def search(answer,x,y,f):
    try:
        if f==0:
            for a in answer:
                if a[0] == x and a[1] == y:
                    return True
                else:
                    return False

        elif f==1:
            for a in answer:
                if a[0] == x and a[1] == y:
                    return True
                else:
                    return False
    except:
        return False
            
def solution(n, build_frame):
    cnt=0
    answer = [[]]
    
    
    for x in build_frame:
        
        
        if x[2] == 0 and x[3] == 1:
            if not search(answer,x[0],x[1]-1,0) and x[1] != 0:
                continue
            else:
                answer.append([[0],x[1],x[2]])
            
        elif x[2] == 0 and x[3] == 0:
            if search(answer,x[0],x[1]+1,0):
                continue
            else:
                answer.append([[0],x[1],x[2]])
            if search(answer,x[0]-1,x[1]+1,1):
                if not search(answer,x[0]-2,x[1]+1,1) or not search(answer,x[0],x[1]+1,1):                   
                    continue  
                else:
                    answer.append([[0],x[1],x[2]])
                    
            else:
                answer.append(x[0],x[1],x[2])
            if  search(answer,x[0],x[1],1):                
                if not search(answer,x[0]-1,x[1]+1,1) or not search(answer, x[0]+1,x[1]+1,1):
                    continue
                    
                else:
                    answer.append([[0],x[1],x[2]])
            else:
                answer.append([[0],x[1],x[2]])
            
            
        elif x[2] == 1 and x[3] == 1:
            if not search(answer,x[0]+1,x[1]-1,0) and not search(answer,x[0],x[1]-1,0):
                if not search(answer,x[0]+1,x[1],1) or not search(answer,x[0]-1,x[1],1):
                    continue
                else:
                    answer.append([[0],x[1],x[2]])
            else:
                answer.append([[0],x[1],x[2]])
                    
                    
        elif x[2] == 1 and x[3] == 0:
            
            if search(answer,x[0]-1,x[1],1):
                if not search(answer,x[0]-1,x[1]-1,0) and not search(answer,x[0],x[1]-1,0):
                    continue
                else:
                    answer.append([[0],x[1],x[2]])
            else:
                answer.append([[0],x[1],x[2]])
            if search(answer,x[0]+1,x[1],1):
                if not search(answer,x[0]+1,x[1]-1,0) and not search(answer,x[0]+2,x[1]-1,0):
                    continue
                else:
                    answer.append([[0],x[1],x[2]])
            else:
                answer.append([[0],x[1],x[2]])
        
            
            
    return answer


b=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n=5
print(solution(n,b))