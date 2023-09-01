//감시 가는한 방향을 다 담아서 백트랙킹 ?
//방향에 경우의 수가 너무 많아서 힘듬
//rotate사용
//각 cctv는 서로에게 영향을 주지 않음 (순서 상관 x)
//1-5의 숫자들의 좌표를 ArrayList에 담고
//그걸 depth로 백트랙킹을 시도
//for문은 각 번호에 맞는 방향의 경우의수로 돌림
//시간복잡도
//일단 cctv가 최대 8개이므로 depth는 최대 8(할 만함)
//cctv의 경우의 수가 많아봤자 3개
//백트랙킹으로 완탐을 시도해도 될 것 같음
//정리
//방향벡터를 큐에 담음(한번 쓰고 poll하고 다시 add할 것임)
//회전 한번 당 벡터 한칸 씩 이동이기 대문에
//1일 때 1방향, 4경우의 수(회전 1번)
//2일 때 2방향, 2경우의 수(회전 2번)
//3일 때 2방향, 4경우의 수(회전 1번)
//4일 때 3방향, 4경우의 수(회전 1번)
//5일 때 4방향, 1경우의 수(회전 4번인데 그럼 제자리니까 회전 x)
//방향은 bfs할 범위 경우의 수는 회전 여부
//1. 방향벡터 설정
//2. ArrayList에 숫자 담기
//3. depth의 숫자의 경우의 수를 범위로 for문을 돌리고
//4. bfs는 숫자의 방향 개수만큼 범위로 돌림
//5. 단 bfs를 돌릴 때 cctv를 통과할 때마다 cnt+1(마지막에 빼줘야함)


import java.util.*;
import java.io.*;
public class 감시{
    //1은 순서 상관x
    //2는 위아 순서로
    //3은 위오
    //4는 위오아
    //5는 순서 상관x
    static Queue[] dx={new LinkedList<Integer>(Arrays.asList(0,0,-1,1)),new LinkedList<Integer>(Arrays.asList(1,-1,0,0)),new LinkedList<Integer>(Arrays.asList(1,0,-1,0)),new LinkedList<Integer>(Arrays.asList(1,0,-1,0)),new LinkedList<Integer>(Arrays.asList(0,0,-1,1))};
    static Queue[] dy={new LinkedList<Integer>(Arrays.asList(1,-1,0,0)),new LinkedList<Integer>(Arrays.asList(0,0,-1,1)),new LinkedList<Integer>(Arrays.asList(0,1,0,-1)),new LinkedList<Integer>(Arrays.asList(0,1,0,-1)),new LinkedList<Integer>(Arrays.asList(1,-1,0,0))};
    static ArrayList<int[]> cctv;
    static int n,m;
    static int[][] matrix;
    static int[][] visitied;
    static int count=0;
    static int minsa=99999999;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st=new StringTokenizer(br.readLine()," ");
        n=Integer.valueOf(st.nextToken());
        m=Integer.valueOf(st.nextToken());
        matrix=new int[n][m];
        visitied=new int[n][m];
        cctv=new ArrayList<>();
        for(int i=0; i<n; i++){
            st=new StringTokenizer(br.readLine()," ");
            for(int j=0; j<m; j++){
                matrix[i][j]=Integer.valueOf(st.nextToken());
                if(matrix[i][j]<=5 && matrix[i][j]>=1){
                    //cctv 담기
                    cctv.add(new int[]{i,j});
                }else if(matrix[i][j]==6){
                    //벽을 세준다(마지막에 사각지대에서 벽을 빼주기 위함)
                    count++;
                }
            }
        }
        back(0);
        System.out.println(minsa-count);

    }
    //depth는 0부터 시작
    public static void back(int depth){
        //try-catch문으로 cctv를 다 체크한 것을 구별함
        try {
            //매 수행 때 마다 사각지대를 체크
            int check = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (visitied[i][j] == 0) {
                        check++;
                    }
                }
            }
            if (check < minsa) {
                minsa = check;
            }
            //현재 cctv의 좌표를 담고
            int[] target = cctv.get(depth);
            int cx = target[0];
            int cy = target[1];
            //현재 cctv의 번호도 담는다
            int cur = matrix[cx][cy];
            //bfs 횟수
            int num = 9999999;
            //경우의 수
            int cases = -1;
            //숫자에 따라 bfs횟수와 경우의 수를 담음
            if (cur == 1) {
                num = 1;
                cases = 4;
            } else if (cur == 2) {
                num = 2;
                cases = 2;
            } else if (cur == 3) {
                num = 2;
                cases = 4;
            } else if (cur == 4) {
                num = 3;
                cases = 4;
            } else if (cur == 5) {
                num = 4;
                cases = 1;
            }
            //사용한 조건을 다시 되돌리기 위한 깊은 복사 행렬을 미리 만들어 놓는다.
            for (int i = 0; i < cases; i++) {
                int[][] tmps = deepCopyMatrix(visitied);
                //dfs를 돌리고
                dfs(cx, cy, num, cur - 1);
                //재귀한다
                back(depth + 1);
                //좌표를 회전하는 과정(deque에서는 rotate를 사용할 수 있음)
                int tmpX = (int) dx[cur - 1].poll();
                int tmpY = (int) dy[cur - 1].poll();
                int tmpx2 = -1;
                int tmpy2 = -1;
                dx[cur - 1].add(tmpX);
                dy[cur - 1].add(tmpY);
                //2일 때는 2번 회전해야함
                if (cur == 2) {
                    tmpx2 = (int) dx[cur - 1].poll();
                    tmpy2 = (int) dy[cur - 1].poll();
                    dx[cur - 1].add(tmpx2);
                    dy[cur - 1].add(tmpy2);
                }
                visitied = tmps;
            }
        }
        //cctv를 끝까지 다 체크해서 예외가 나오면 return
        catch(Exception e){
            return;
        }
    }
    //깊은 복사 함수
    public static int[][] deepCopyMatrix(int [][] a){
        int[][] tmp = new int[n][m];
        for(int i=0; i<n;i++){
            for(int j=0; j<m; j++){
                tmp[i][j]=a[i][j];
            }
        }
        return tmp;
    }
    //dfs(모든 노드를 탐색하는 것이 목적이 아님)
    public static void dfs(int x,int y,int num,int cur){
        ArrayDeque<int []> q=new ArrayDeque<>();
        int cn=0;
        //이터레이터로 좌표를 순회할 것임
        Iterator dxx = dx[cur].iterator();
        Iterator dyy = dy[cur].iterator();
        visitied[x][y]=1;
        //방향 수 만큼 일직선으로 탐색 수행
        for(int i=0; i<num; i++){
            //이터레이터에서 꺼내서 이동할 벡터를 담아줌
            int gox=(int) dxx.next();
            int goy=(int) dyy.next();
            //이동한 좌표를 담음
            int nx=x+gox;
            int ny=y+goy;
            //이동한 좌표를 일직선으로 깊게 탐색
            while(true){
                if(nx<0 || nx>=n || ny<0 || ny>=m){
                    break;
                }
                if(matrix[nx][ny]==6){
                    break;
                }
                visitied[nx][ny]=1;
                nx+=gox;
                ny+=goy;
            }
        }
    }
}

