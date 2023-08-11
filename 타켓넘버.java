//아이디어
//백트랙킹, 완전탐색으로도 풀릴 것 같으나 조건이 추가되지 않고 +,-일때의 가중치가 같으므로 DFS,BFS로도 충분히 풀릴 것으로 보임
//target부터 시작해서 0이 도달할 때까지로 하겠음
//가지치기는 +,-로 한다.
//모든 경우의 수를 판별하는 문제이다.
//DFS로 해결하겠다.
import java.util.*;
class 타겟넘버 {    
    static int cnt=0;    
    public int solution(int[] numbers, int target) {                
        back(target,0,numbers);
        return cnt;
    }
    public void back(int result,int depth,int[] numbers){     
        //depth가 끝까지 도달했는데 값이 0이라면 cnt+1
        if (depth==numbers.length){
            if(result==0){
                cnt+=1;
            }
            return;
        }        
        for(int i=0; i<2; i++){
            if (i==0){
                result+=numbers[depth];
                back(result,depth+1,numbers);
                result-=numbers[depth];
            }else{
                result-=numbers[depth];
                back(result,depth+1,numbers);
                result+=numbers[depth];
            }                   
        }        
    }
}