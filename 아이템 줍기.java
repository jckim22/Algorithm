//아이디어
//가중치가 1인 간격으로 테두리를 따라가는 BFS 풀이를 할 것이다.
//ㄷ자 모양에서는 없는 경로로 바로 이동할 수 있으므로 한 칸 띄워주기 위해서 좌표를 x2 해준다.
//먼저 모든 사각형의 위치를 1로 바꾸어준다.
//그리고 사각형마다 내부를 0으로 바꾸어 준다면 사각형들이 모여있는 테두리만 남게 된다.
//시간복잡도
//노드는 100x100으로 최대 1만개, 간선은 상하좌우 4방향이므로 4x100x100, 10,000 + 40,000= 50,000
//O(v+e)= 50,000 정도로 예상된다.

// System.out.printf("%d ",a);
// System.out.println();
import java.util.*;
class Solution {
    static int[][] matrix;
    static int[][] visited;
    static int answer;
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        //2배 늘린 크기로 matrix 할당
        matrix=new int[101][101];
        //사각형을 1로 채우는 과정
        for(int[] temp:rectangle){
            for(int i=temp[1]*2; i<=temp[3]*2; i++){
                for(int j=temp[2]*2; j>=temp[0]*2; j--){
                    matrix[i][j]=1;
                }
            }
        }
        //내부를 0으로 채우는 과정(껍데기만 남게됨)
        for(int[] temp:rectangle){
            for(int i=temp[1]*2+1; i<=temp[3]*2-1; i++){
                for(int j=temp[2]*2-1; j>=temp[0]*2+1; j--){
                    matrix[i][j]=0;
                }
            }
        }
        answer=bfs(characterY*2,characterX*2,itemY*2,itemX*2);
        //         for(int[] temp:matrix){
        //     for(int tmp:temp){
        //         System.out.printf("%d ",tmp);                
        //     }
        //     System.out.println();
        // }
        
        //정답의 나누기 2
        return answer/2;                        
    }
    public static int bfs(int x, int y,int ix,int iy){
        //방문 매트릭스 할당
        visited=new int[101][101];        
        //큐에 캐릭터 시작 위치 담음
        Queue<int[]> q=new LinkedList<>();
        q.add(new int[]{x,y});
        //방문처리
        visited[x][y]=1;
        int[] dx={-1,1,0,0};
        int[] dy={0,0,-1,1};
        while(!q.isEmpty()){
            int[] z=q.poll();            
            for(int i=0; i<4;i++){
                int nx=z[0]+dx[i];
                int ny=z[1]+dy[i];
                //다음 좌표가 범위를 초과했을 때(좌표는 1이상 50이하)
                if(nx<2 || nx>100 || ny<2 || ny>100){
                    continue;
                }
                //방문을 했을 때
                if(visited[nx][ny]==1){
                    continue;
                }
                //가려고 하는 곳이 1이 아닌 곳(껍데기가 아닌 곳)
                if(matrix[nx][ny]!=1){
                    continue;
                }
                //다 통과했다면 방문 처리 후 거리 계산
                q.add(new int[]{nx,ny});
                matrix[nx][ny]=matrix[z[0]][z[1]]+1;
                visited[nx][ny]=1;
            }
        }
        return matrix[ix][iy];
    }
} 
