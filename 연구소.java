import java.util.*;
import java.io.*;
public class 연구소{
    static int n,m;
    //행렬의 크기는 정해져 있으므로 2차원 배열
    static int matrix[][];
    static int matrixx[][];
    //safe나 virus는 입력 값에 따라 크기가 달라질 것이므로 int[]를 요소로 하는 Arraylist로 생성
    static ArrayList<int[]> safe;
    static ArrayList<int[]> virus;
    static int max;
    static int dx[]={-1,1,0,0};
    static int dy[]={0,0,-1,1};
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        //고정된 크기의 행렬에 배열 할당
        matrix=new int[n][m];
        matrixx=new int[n][m];
        //virus와 safe에 arraylist 할당
        virus = new ArrayList<>();
        safe = new ArrayList<>();
        //행렬 만들기
        for(int i=0; i<n;i++){
            for(int j=0; j<m; j++){
                int a=sc.nextInt();
                matrix[i][j]=a;
                matrixx[i][j]=a;
            }
        }
        //안전한 곳과 virus의 위치를 배열 형태로 append
        for(int i=0; i<n;i++){
            for(int j=0; j<m; j++){
                if (matrix[i][j]==0){
                    safe.add(new int[]{i,j});
                }
                if (matrix[i][j]==2){
                    virus.add(new int[]{i,j});
                }
            }
        }
        back(0,0);
        System.out.println(max);

    }
    public static int bfs(){
        //배열을 요소로 받는 큐 생성
        Queue <int[]> q=new LinkedList<>();
        for(int i=0; i<virus.size();i++){
            int tmp[]=virus.get(i);
            q.add(tmp);
        }
        while(!q.isEmpty()){
            int tmp[]=q.poll();
            int x=tmp[0];
            int y=tmp[1];
            for(int i=0; i<4;i++){
                int nx=x+dx[i];
                int ny=y+dy[i];
                if(nx<0 || nx>=n || ny <0 || ny>=m){
                    continue;
                }
                if(matrix[nx][ny]==2 || matrix[nx][ny]==1){
                    continue;
                }
                matrix[nx][ny]=2;
                q.add(new int[]{nx,ny});
            }
        }
        return checksafe();
    }
    public static int checksafe(){
        int cnt=0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(matrix[i][j]==0){
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
    public static void back(int depth, int idx){
        if (depth==3){
            //새로운 matrix에 matrixx(원본) 행렬을 복사
            matrix=new int[n][m];
            for(int i=0;i<n;i++){
                for(int j=0; j<m;j++){
                    matrix[i][j]=matrixx[i][j];
                }
            }
//            System.out.println("first");
//            for(int i=0;i<n;i++){
//                for(int j=0;j<m;j++) {
//                    System.out.printf("%d ", matrix[i][j]);
//                }
//                System.out.println();
//            }
            int tmp=bfs();

            if (tmp>max){
                max=tmp;
            }
//            System.out.println("second");
//            for(int i=0;i<n;i++){
//                for(int j=0;j<m;j++) {
//                    System.out.printf("%d ", matrix[i][j]);
//                }
//                System.out.println();
//            }
//            System.out.println();

            return;
        }
        for(int i=idx; i<safe.size();i++){
            int tmp[]=safe.get(i);
            //원본 배열의 벽을 조작
            matrixx[tmp[0]][tmp[1]]=1;
            back(depth+1,i+1);
            matrixx[tmp[0]][tmp[1]]=0;
        }
    }
}

