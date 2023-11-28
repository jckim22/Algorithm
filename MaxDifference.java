import java.util.*;
import java.io.*;

public class MaxDifference{
    static int n;
    static int[] arr;
    static int sum=0;
    static int maxSum = -1;
    static LinkedList<Integer> containCheck;
    static LinkedList<Integer> lis;
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine()," ");
        arr = new int[n];
        lis = new LinkedList<>();
        containCheck = new LinkedList<>();
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        back(0);
        System.out.println(maxSum);
    }
    public static void back(int depth){
        if(depth == n){
            sum=0;
            for(int i=1; i<n; i++){
                sum += Math.abs(lis.get(i-1) - lis.get(i));
            }
            if(maxSum<sum){
                maxSum=sum;
            }
        }
        for(int i = 0; i<n; i++){
            if(containCheck.contains(i)){
                continue;
            }
            lis.add(arr[i]);
            containCheck.add(i);
            back(depth+1);
            lis.pollLast();
            containCheck.pollLast();
        }
    }
}
