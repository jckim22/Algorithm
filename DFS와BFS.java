import java.util.*;
import java.io.*;
public class DFS와BFS {
    static int n, m, v;
    //graph배열을 선언 다만 객체로는 Integer타입의 요소를 받는 ArrayList가 들어올 수 있음
    static ArrayList<Integer> graph[];
    //visited 변수를 선언 다만 객체로는 boolean타입의 요소를 받는 ArrayList가 들어올 수 있음
    static ArrayList<Boolean> visited;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();
        //graph 배열에 ArrayList의 공간을 n+1만큼 할당하겠다.
        graph = new ArrayList[n + 1];
        //visited변수에 ArrayList의 공간을 할당하겠다.
        visited = new ArrayList<>();
        for(int i=0; i<n+1;i++){
            //visited에 false를 append
            visited.add(false);
        }
        for(int i=0; i<n+1; i++){
            //ArrayList의 공간을 n+1개만큼 할당했으니 각각 할당된 공간에 ArrayList의 공간을 할당한다.(2차원ArrayList)
            graph[i]=new ArrayList<>();
        }
        //간선을 입력 받아 인덱스 기준 정점의 그래프 완성
        for(int i=0; i<m; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }
        //sort
        for(int i=0; i<graph.length;i++){
            Collections.sort(graph[i]);
        }
        dfs(v);
        System.out.println();
        bfs();
    }
    public static void dfs(int idx){
        if (visited.get(idx)){
            return;
        }
        visited.set(idx,true);
        System.out.printf("%d ",idx);
        for(int i = 0; i<graph[idx].size(); i++){
            dfs(graph[idx].get(i));
        }
    }
    public static void bfs(){
        //Integer 타입의 요소를 받는 Queue 객체를 받을 수 있는 변수 q에 LinkedList 객체를 할당한다.
        Queue<Integer> q=new LinkedList<>();
        //큐에 시작정점을 append
        q.add(v);
        //방문처리
        visited.set(v,false);
        System.out.printf("%d ",v);
        while(!q.isEmpty()){
            //q에서 pop한다
            int idx=q.poll();
            for(int i=0;i<graph[idx].size();i++){
                if(!visited.get(graph[idx].get(i))){
                  continue;
                }
                System.out.printf("%d ",graph[idx].get(i));
                q.add(graph[idx].get(i));
                visited.set(graph[idx].get(i),false);
            }
        }
    }
}