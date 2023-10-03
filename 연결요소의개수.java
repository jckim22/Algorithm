//아이디어
//정점 만큼의 ArrayList 배열을 생성한다.
//ArrayList에 간선에 따라서 연결된 노드들을 추가한다.
//그렇게 그래프를 완성하고 bfs를 돌릴 때마다 연결 요소를 +1 해준다.

import java.io.*;
import java.util.*;

public class 연결요소의개수{
    static ArrayList<Integer>[] graph;
    static int[] visited;
    static int n,m;
    static int u,v;
    static int answer=0;
    public static void main(String[] args)throws IOException{
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st=new StringTokenizer(br.readLine());
        n=Integer.valueOf(st.nextToken());
        m=Integer.valueOf(st.nextToken());
        //그래프에 ArrayLIst 배열을 정점만큼 할당
        graph=new ArrayList[n+1];
        visited=new int[n+1];
        //각 그래프의 노드에 ArrayList를 할당
        for(int i=1;i<n+1;i++){
            graph[i]=new ArrayList<>();
        }
        for(int i=0; i<m; i++){
            st=new StringTokenizer(br.readLine());
            u=Integer.valueOf(st.nextToken());
            v=Integer.valueOf(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }
//        for(int i=1; i<n+1; i++){
//            System.out.printf("%d: ",i);
//            for(int tmp:graph[i]){
//                System.out.printf("%d ",tmp);
//            }
//            System.out.println();
//        }
        for(int i=1 ;i<n+1; i++){
            if(visited[i]==0){
                bfs(graph[i]);
                answer++;
            }
        }
        System.out.println(answer);
    }
    public static void bfs(ArrayList start){
        ArrayDeque<ArrayList> q=new ArrayDeque<>();
        q.add(start);
        while(!q.isEmpty()){
            ArrayList<Integer> na=q.pollFirst();
            for(int i=0; i<na.size(); i++){
                int nc=na.get(i);
                if(visited[nc]==1){
                    continue;
                }
                visited[nc]=1;
                q.add(graph[nc]);
            }
        }
    }
}