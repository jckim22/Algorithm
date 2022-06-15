#include <iostream>
#include <vector>
#include <queue>
#define MAX 10

using namespace std;

int n, inDegree[MAX]; //inDgree는 진입차수
vector<int> a[MAX]; //정점

void topologySort() {
	int result[MAX]; //위상정렬의 결과를 담을 배열
	queue<int> q; //임시로 담아줄 큐 선언
	
	for (int i = 1; i <= n; i++) {
		if (inDegree[i] == 0) {//만약 진입차수가 0이라면
			q.push(i); //큐에 담아준다
		}
	}

	for (int i = 1; i <= n; i++) { //시작하기도 전에 큐가 비어있다면 진입차수가 0인 정점이 없다는 것
		if (q.empty()) {
			printf("사이클이 발생했습니다.");//그렇다는건 사이클이 발생했다는 것이다.
			return;
		}
		int x = q.front();//사이클이 없다면 큐의 가장 먼저 들어온 값을 x에 담아주고
		q.pop(); //큐에서 뺀다
		result[i] = x; //큐에서 뺀 순서가 결국 위상정렬의 순서이므로 결과에 담아준다
		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i]; //진입차수가 0인 값의 인접노드를 넣어주고
			if (--inDegree[y] == 0) { //그 인접노드의 진입차수를 1빼주고 그렇게 해서 진입차수가 혹시 0이라면
				q.push(y); //큐에 다시 넣어준다
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", result[i]);
	}

}

int main() {
	n = 7;
	a[1].push_back(2); //2에다가 1을 연결
	inDegree[2]++; //2의 진입차수는 1증가
	a[1].push_back(5);
	inDegree[5]++;
	a[2].push_back(3);
	inDegree[3]++;
	a[3].push_back(4);
	inDegree[4]++;
	a[4].push_back(6);
	inDegree[6]++;
	a[5].push_back(6);
	inDegree[6]++;
	a[6].push_back(7);
	inDegree[7]++;
	topologySort();
}