import java.util.*;
import java.io.*;
public class Main{    
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int target = sc.nextInt();
    int n = sc.nextInt();
    int total=0;
    for(int i =0; i<n; i++){
      int a=sc.nextInt();
      int b=sc.nextInt();
      total+=a*b;      
    }
    if(total==target){
      System.out.println("Yes");
    }
    else{
      System.out.println("No") ;
    }
  }
}