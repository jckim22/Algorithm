import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;
import java.lang.*;
//아이디어
//최소 크기는 2x2
//matrix를 나누는 것 중요함
//divide(srow,scol,n//2)
//divide(srow,scol+n//2,n//2)
//divide(srow+n//2,scol,n//2)
//divide(srow+n//2,scol+n//2,n//2)
//위 형태로 쪼개면 될 듯
//n이 1이면 리턴
//방문할 때 마다 카운트를 하고 특정 행렬에 도달하면 그 숫자를 출력하고 리턴
public class z {
    static int[][] matrix;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N,r,c;
        st=new StringTokenizer(br.readLine()," ");
        N=Integer.valueOf(st.nextToken());
        r=Integer.valueOf(st.nextToken());
        c=Integer.valueOf(st.nextToken());
        int n=(int)Math.pow(2,N);
        divide(r,c,n,r,c);
        System.out.println(cnt);
     }
    public static void divide(int trow,int tcol,int n,int row,int col) {
        if(n == 1){
            return;
        }
        if(row < n/2 && col < n/2) {
            divide(trow,tcol,n/2, row, col);
        }
        else if(row < n/2 && col >= n/2) {
            cnt += n * n / 4;
            divide(trow,tcol,n/2, row, col - n/2);
        }
        else if(row >= n/2 && col < n/2) {
            cnt += (n * n / 4) * 2;
            divide(trow,tcol,n/2, row - n/2, col);
        }
        else {
            cnt += (n * n / 4) * 3;
            divide(trow,tcol,n/2, row - n/2, col - n/2);
        }
    }
}