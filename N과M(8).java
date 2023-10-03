import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;
//아이디어
//배열에 수들을 담고 정렬한다.
//n만큼 반복을 시작하고 depth가 m이 되면 담긴 배열을 출력한다.
//그리고 돌아오면서 조건을 삭제한다.

public class N과M {
    static int n,m;
    static ArrayList<Integer> arr;
    static ArrayDeque<Integer> tmp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st=new StringTokenizer(br.readLine()," ");
        n=Integer.valueOf(st.nextToken());
        m=Integer.valueOf(st.nextToken());
        arr=new ArrayList<>();
        tmp=new ArrayDeque<>();
        st=new StringTokenizer(br.readLine()," ");
        for(int i=0; i<n; i++){
            arr.add(Integer.valueOf(st.nextToken()));
        }
        Collections.sort(arr,new Comparator<Integer>(){
            @Override
            public int compare(Integer s1, Integer s2){
                return s1-s2;
            }
        });
        back(0,0);
    }
    public static void back(int depth,int idx){
        if(depth == m){
            for(int a:tmp){
                System.out.printf("%d ",a);
            }
            System.out.println();
            return;
        }
        for(int i=idx; i<n; i++){
            tmp.add(arr.get(i));
            back(depth+1,i);
            tmp.pollLast();
        }
    }
}