import java.util.*;
import java.io.*;
public class 문자열집합{
    static int n,m;
    static String s[];
    static int cnt=0;
    static Map<String,Integer> hs;
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        sc.nextLine();
        hs=new HashMap<>();
        s=new String[n+1];
        for(int i=0; i<n; i++){
            hs.put(sc.nextLine(),0);
        }
        for(int j=0; j<m; j++){
            String tmp=sc.nextLine();
            if(hs.containsKey(tmp)){
                cnt+=1;
            }
        }
        System.out.println(cnt);
    }
}