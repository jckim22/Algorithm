//아이디어:
//먼저 컴퓨터의 수만큼 배열을 생성한
//연결되어 있는 노드를 배열에 담는다.
//방문확인 배열도 컴퓨터의 수만큼 생성한다.
//그 후 1번부터 BFS를 진행하고
//방문되어 있는 컴퓨터의 수 -1을 출력한다.
//bfs돌릴 떄 각 컴퓨터의 연결되어 있는 노드 수만큼 반복한다.
//방문되어 있으면 continue
//시간복잡도
//컴퓨터의 수가 100개 이하이다. 충분하다.
//자료구조
//그래프 = int [][]
//방문확인 = int []

import java.util.*;
import java.io.*;

public class 바이러스{
    static ArrayList<Integer>[] graph;
    static int visited[];
    static int n;
    static int m;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n=Integer.valueOf(br.readLine());
        m=Integer.valueOf(br.readLine());
        //ArrayList 배열을 graph에 할당
        graph=new ArrayList[n+1];
        //방문 배열 할당
        visited=new int[n+1];
        //각 배열의 요소에 ArrayList 할당
        for(int i=1;i<n+1;i++){
            graph[i]=new ArrayList<>();
        }
        for(int i=0; i<m; i++){
            st=new StringTokenizer(br.readLine()," ");
            int j=Integer.valueOf(st.nextToken());
            int h=Integer.valueOf(st.nextToken());
            graph[j].add(h);
            graph[h].add(j);
        }
//        for(int i=1; i<n+1; i++){
//            int sz=graph[i].size();
//            System.out.printf("%d ",i);
//            for(int j=0; j<sz; j++){
//                System.out.printf("%d ",graph[i].get(j));
//            }
//            System.out.println();
//        }
        bfs();
        int cnt=0;
        for(int i=1; i<n+1;i++){
            if(visited[i]==1){
                cnt++;
            }
        }
        System.out.println(cnt-1);
    }
    static void bfs(){
        ArrayDeque<ArrayList> q=new ArrayDeque<>();
        q.add(graph[1]);
        visited[1]=1;
        while(!q.isEmpty()){
            ArrayList<Integer> cur=q.pollFirst();
            for(int i=0; i<cur.size(); i++){
                int nc=cur.get(i);
                if(visited[nc]!=0){
                    continue;
                }
                visited[nc]=1;
                q.add(graph[nc]);
            }
        }
    }
}