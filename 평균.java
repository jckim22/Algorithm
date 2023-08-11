import java.util.*;
import java.io.*;
public class 평균{
    public static void main(String args[]){
        ArrayList<Integer> arr = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            int a = sc.nextInt();
            arr.add(a);
        }
        int total=0;
        for(int i=0; i<arr.size(); i++){
            total+=arr.get(i);
        }
        System.out.println(total/n);
    }
}