import java.util.*;
import java.io.*;
//아이디어:
//1. 먼저 아기 상어를 기준으로 bfs를 돌려서 distance[][]에 거리들을 저장해놓은다.
//2. n이 작으므로 distance와 matrix를 완탐하여 먹기 가장 알맞은 물고기를 고른다.
//3. 그 물고기 자리에 아기 상어를 위치하게 하고 아기 상어의 뱃속을 +1 해준다.(아기 상어의 뱃속이 상어의 크기와 같다면 상어 +1)
//4. 이후 distance를 초기화한 후 다시 1번 과정으로 돌아가서 이 과정을 반복한다.
//5. 먹을 물고기가 없다면 종료
//시간복잡도
//n=20이라 bfs 문제 없고 완탐을 돌려도 문제 없다.
public class 아기상어{
    static int[][] matrix,distance;
    static ArrayDeque<int[]> q;
    static int x,y;
    static int n;
    static int shark=2;
    static int sharkSto=0;
    static int answer=0;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n=Integer.valueOf(br.readLine());
        StringTokenizer st;
        matrix= new int[n][n];
        distance=new int[n][n];

        for(int i=0; i<n; i++){
            st=new StringTokenizer(br.readLine()," ");
            for(int j=0; j<n; j++){
                matrix[i][j]=Integer.valueOf(st.nextToken());
                if(matrix[i][j]==9){
                    x=i;
                    y=j;
                    matrix[i][j]=-1;
                }
            }
        }
        while(true){
            //distance 초기화
            distance=new int[n][n];
            //아기 상어의 좌표 구하기
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    if(matrix[i][j]==-1){
                        x=i;
                        y=j;
                    }
                }
            }
            //아기 상어 기준으로 거리 구하기
            bfs();

            ArrayList<int[]> canEatFish=new ArrayList<>();
            ArrayList<int[]> minDisFish=new ArrayList<>();
            //먹을 수 있는 물고기 구하기
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    //상어보다 작고, 상어가 아니고, 비어있는 공간도 아니고, 갈 수 없는 곳도 아니고, 출발 지점도 아닌
                    if(matrix[i][j]<shark && matrix[i][j] != -1 && matrix[i][j]!=0 && distance[i][j]!=0 && distance[i][j]!=1){
                        canEatFish.add(new int[]{i,j});
                    }
                }
            }
            //만약 먹을 수 있는 물고기가 없다면
            if(canEatFish.isEmpty()){
                break;
            }
            int[] targetFish=new int[2];
            int minDistance=99999;
            int minRow=99999;
            int minCol=99999;

            ArrayList<int[]> canEatFishFirst=new ArrayList<>();
            ArrayList<int[]> canEatFishSecond=new ArrayList<>();
            //그 중 현재 가장 적합한 물고기 구하기
            //가장 가까운 거리의 물고기 구하기
            if(canEatFish.size()>1){
                //가까운 거리 구하고
                for(int[] curr:canEatFish){
                    if(distance[curr[0]][curr[1]]<=minDistance){
                        minDistance=distance[curr[0]][curr[1]];
                    }
                }
                //해당하는 물고기 add
                for(int[] curr:canEatFish){
                    if(distance[curr[0]][curr[1]]==minDistance){
                        canEatFishFirst.add(new int[]{curr[0],curr[1]});
                    }
                }
            }else{
                targetFish=canEatFish.get(0);
            }
            //그 중 가장 위쪽
            if(canEatFishFirst.size()>1){
                for(int[] curr:canEatFishFirst){
                    if(curr[0]<=minRow){
                        minRow=curr[0];
                    }
                }
                for(int[] curr:canEatFishFirst){
                    if(curr[0]==minRow){
                        canEatFishSecond.add(new int[]{curr[0],curr[1]});
                    }
                }
            }else{
                if(!canEatFishFirst.isEmpty()){
                    targetFish=canEatFishFirst.get(0);
                }
            }
            //그게 여러개라면 그 중 가장 왼쪽
            if(canEatFishSecond.size()>1){
                for(int[] curr:canEatFishSecond){
                    if(curr[1]<minCol){
                        minCol=curr[1];
                        targetFish=new int[]{curr[0],curr[1]};
                    }
                }

            }
            else{
                if(!canEatFishSecond.isEmpty()){
                    targetFish=canEatFishSecond.get(0);
                }

            }
            answer+=distance[targetFish[0]][targetFish[1]]-1;
            matrix[x][y]=0;
            matrix[targetFish[0]][targetFish[1]]=-1;
            //shark크기 1 증가
            sharkSto++;
            if(sharkSto==shark){
                shark++;
                sharkSto=0;
            }

        }
        System.out.println(answer);
     }
    public static void bfs(){
        q=new ArrayDeque<>();
        q.add(new int[]{x,y});
        int[] dx={-1,1,0,0};
        int[] dy={0,0,-1,1};
        distance[x][y]=1;
        while(!q.isEmpty()){
            int[] cur=q.pollFirst();
            int cx=cur[0];
            int cy=cur[1];
            for(int i=0; i<4; i++){
                int nx=cx+dx[i];
                int ny=cy+dy[i];
                if(nx<0 || nx>=n || ny<0 || ny>=n ){
                    continue;
                }
                if(distance[nx][ny]!=0){
                    continue;
                }
                //shark보다 크면 갈 수 없다.
                if(matrix[nx][ny]>shark){
                    continue;
                }
                distance[nx][ny]=distance[cx][cy]+1;
                q.add(new int[]{nx,ny});
            }
        }
    }
}
