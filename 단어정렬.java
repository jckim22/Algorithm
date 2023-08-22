import java.util.*;
import java.io.*;
public class 단어정렬{
    static String[] arr;
    public static void main(String args[]) throws IOException {
        //버퍼리더 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //한 줄은 정수형으로
        int n=Integer.valueOf(br.readLine());
        //한 줄 받은 문자열 토큰(공백 기준 나누기 위해, 이 문제에서는 불필요)
        StringTokenizer st;
        //배열에 새로운 객체 할당
        arr=new String[n];
        for(int i=0; i<n; i++){
            //한 줄 입력 받는다.
            st=new StringTokenizer(br.readLine());
            //배열에 넣기
            arr[i]=st.nextToken();
        }
        //Set으로 형변환해 중복을 제거한다.
        //asList로 arr을 먼저 리스트로 형변환 뒤 set으로 바꾸어준다.
        Set<String> se = new HashSet<>(Arrays.asList(arr));
        //다시 toArray로 배열로 형변환 해준다.
        //배열의 크기를 0으로 지정해주면 크기는 알아서 할당된다.
        arr=se.toArray(new String[0]);

        //Comparator의 compare를 오버라이딩하여 정렬 조건을 재정의 하여 정렬한다.
        Arrays.sort(arr, new Comparator<String>(){
            @Override
           public int compare(String s1, String s2){
               if(s1.length()==s2.length()){
                   //오름차순
                   return s1.compareTo(s2);
               }else{
                   //길이 오름차순
                   return s1.length()-s2.length();
               }
           }
        });
        //arr을 출력
        for(String s:arr){
            System.out.println(s);
        }
    }
}