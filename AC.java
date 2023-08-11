import java.util.*;
import java.io.*;
public class AC{
    static ArrayDeque<Integer> q;
    static int t;
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        t=sc.nextInt();
        sc.nextLine();
        for(int i=0; i<t;i++){
            boolean mode=true;
            boolean check=true;
            boolean cc=false;
            String func=sc.next();
            sc.nextLine();
            int n=sc.nextInt();
            sc.nextLine();
            String arr=sc.next();
            sc.nextLine();
            //substring으로 양쪽의 대괄호를 잘라준다.
            arr=arr.substring(1,arr.length()-1);
            //함수중에서 'D'가 존재하면  cc를 true로 체크
            for(int j=0; j<func.length(); j++){
                if(func.charAt(j)=='D'){
                    cc=true;
                    break;
                }
            }
            //대괄호를 제거해도 남는게 있다면 숫자가 있는 것이므로
            if(!arr.isEmpty()){
                //숫자들을 ,기준으로 나눠주고
                String[] qs=arr.split(",");
                //q에 하나씩 String을 Integer.valueOf로 형변환하면서 삽입한다.
                q=new ArrayDeque<>();
                for(int j=0; j<qs.length;j++){
                    q.add(Integer.valueOf(qs[j]));
                }
            }
            //arr이 대괄호를 제거하니 비어있고 함수 중에 D가 없으면 답은 빈괄호일 것이므로 []를 반환
            else if(arr.isEmpty() && !cc){
                System.out.println("[]");
                continue;
            }
            //그것도 아니라면 arr이 비었는데 함수 D가 있을 것이므로 error 출력
            else{
                System.out.println("error");
                continue;
            }
            //함수의 길이만큼 반복함
            for(int j=0; j<func.length();j++){
                //mode에 따라서 왼쪽인지 오른쪽 pop인지 결정
                if (func.charAt(j) == 'R'){
                    mode=!mode;
                }
                else if(func.charAt(j)=='D'){
                    if (mode){
                        if (!q.isEmpty()){
                            q.pollFirst();
                        }
                        else{
                            check=false;
                            System.out.println("error");
                            break;
                        }
                    }
                    else{
                        if (!q.isEmpty()){
                            q.pollLast();
                        }
                        else{
                            check=false;
                            System.out.println("error");
                            break;
                        }
                    }
                }
            }
            if (!check){
                continue;
            }
            if(q.isEmpty()){
                System.out.println("[]");
                continue;
            }
            //답을 출력하기 위해 StringBuilder를 사용
            StringBuilder sb=new StringBuilder();
            sb.append("[");
            if(mode){
                while(!q.isEmpty()){
                    sb.append(q.pollFirst());
                    sb.append(",");
                }
            }
            else{
                while(!q.isEmpty()){
                    sb.append(q.pollLast());
                    sb.append(",");
                }
            }
            //마지막 쉼표 제거 후 닫는 대괄호를 append
            sb.deleteCharAt(sb.length()-1);
            sb.append("]");
            System.out.println(sb);
        }
    }
}