class 네트워크 {
    static boolean[] visited;
    public int solution(int n, int[][] computers) {        
        int answer = 0;
        visited=new boolean[n+1];        
        for(int i=0;i<n;i++){
            visited[i]=false;
        }
        for(int i=0;i<n;i++){
            if(!visited[i]){
                dfs(i,n,visited,computers);    
                answer+=1;
            }
        }
        
        return answer;
    }
    public void dfs(int idx,int n,boolean[] visited,int[][] computers){
        if(visited[idx] == true){
            return;
        }
        visited[idx]=true;
        for(int i=0;i<n;i++){
            if(computers[idx][i]==0){
                continue;
            }
            if(idx==i){
                continue;
            }
            dfs(i,n,visited,computers);
        }
    }
}