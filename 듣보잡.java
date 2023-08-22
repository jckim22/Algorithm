import java.util.*;
import java.io.*;
//아이디어:
//HashMap을 사용해서 두번의 체크과정 동안 두번 다 체크된 key값들을 정렬하여 출력한다.
public class 듣보잡{
    //HashMap을 받을 변수 선언
    static Map<String,Integer> dic;
    //유동적인 어레이리스트를 선언
    static ArrayList<String> answer;
    public static void main(String args[]) throws IOException {
     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     StringTokenizer st;
     st=new StringTokenizer(br.readLine()," ");
     int n=Integer.valueOf(st.nextToken());
     int m=Integer.valueOf(st.nextToken());
     //HashMap과 ArrayList 할당
     dic=new HashMap<>();
     answer=new ArrayList<>();
     //HashMap에 value를 1로 할당
     for(int i=0; i<n; i++){
         st=new StringTokenizer(br.readLine(), " ");
         String tmp=st.nextToken();
         dic.put(tmp,1);
     }
     //만약 키를 갖고 있다면 갖고 있던 수에 +1
     for(int i=0; i<m;i++){
         st=new StringTokenizer(br.readLine(), " ");
         String tmp=st.nextToken();
         if(dic.containsKey(tmp)){
             dic.put(tmp,dic.get(tmp)+1);
         }
     }
     //Map.Entry로 HashMap을 하나씩 받음
     for(Map.Entry<String,Integer> entry:dic.entrySet()){
         //Value가 1보다 크면 두번정도 나온 것이므로 answer리스트에 add
         if (entry.getValue()>1){
             answer.add(entry.getKey());
         }
     }
     //새로운 배열에 형변환
     String[] answers=answer.toArray(new String[0]);
     //배열을 오름차순으로 정렬
     Arrays.sort(answers);
     System.out.println(answers.length);
     for(String s:answers){
         System.out.println(s);
     }
    }
}