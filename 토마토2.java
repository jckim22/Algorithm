import java.io.*;
import java.util.*;
public class 토마토2 {
    static int x,y,z;
    static ArrayDeque<int[]> q;
    static ArrayList<int[]> tomato;
    static int[] dz = {1, -1, 0, 0, 0, 0};
    static int[] dy = {0, 0, 1, -1, 0, 0};
    static int[] dx = {0, 0, 0, 0, 1, -1};
    static int[][][] matrix;
    static int[][][] visited;
    static int min=999999999;
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st=new StringTokenizer(br.readLine()," ");
        y=Integer.valueOf(st.nextToken());
        x=Integer.valueOf(st.nextToken());
        z=Integer.valueOf(st.nextToken());
        matrix=new int[z][x][y];
        visited=new int[z][x][y];
        tomato=new ArrayList<>();
        for(int h=0; h<z; h++) {
            for (int i = 0; i < x; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < y; j++) {
                    matrix[h][i][j] = Integer.valueOf(st.nextToken());
                    if (matrix[h][i][j] == 1) {
                        tomato.add(new int[]{h,i,j});
                        visited[h][i][j] = 1;
                    }
                }
            }
        }
        boolean check=true;
        for(int i=0;i<z;i++){
            for(int j=0;j<x;j++){
                for(int c=0;c<y;c++){
                    if(matrix[i][j][c]==0){
                        check=false;
                    }
                }
            }
        }
        if(check){
            System.out.println(0);
            return;
        }
        boolean check2=true;
        int max=-999;
        bfs();
        for(int i=0;i<z;i++){
            for(int j=0;j<x;j++){
                for(int c=0;c<y;c++){
                    if(visited[i][j][c]>max){
                        max=visited[i][j][c];
                    }
                    if(visited[i][j][c]==0 && matrix[i][j][c]!=-1){
                        check2=false;
                    }
                }
            }
        }
        if(!check2){
            System.out.println(-1);
            return;
        }
        System.out.println(max-1);
    }
    static void bfs(){
        q=new ArrayDeque<>();
        for(int i=0; i<tomato.size(); i++){
            q.add(tomato.get(i));
        }
        while(!q.isEmpty()){
            int[] cur=q.pollFirst();
            int cz=cur[0];
            int cx=cur[1];
            int cy=cur[2];
            for (int i = 0; i < 6; i++) {
                int nz= cz + dz[i];
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nz<0||nz>=z||nx < 0 || nx >= x || ny < 0 || ny >= y) {
                    continue;
                }
                if (matrix[nz][nx][ny] == 1) {
                    continue;
                }
                if (visited[nz][nx][ny] > 0) {
                    continue;
                }
                if (matrix[nz][nx][ny] == -1) {
                    continue;
                }
//                for(int q=0;q<z;q++){
//                    for(int j=0;j<x;j++){
//                        for(int c=0;c<y;c++){
//                            System.out.printf("%d ",visited[q][j][c]);
//                        }
//                        System.out.println();
//                    }
//                    System.out.println();
//                }
//                System.out.println(visited[nz][nx][ny]);
//                System.out.println(visited[cz][cx][cy]);
                matrix[nz][nx][ny] = 1;
                visited[nz][nx][ny] = visited[cz][cx][cy] + 1;

                q.add(new int[]{nz,nx, ny});
            }
        }
    }
}