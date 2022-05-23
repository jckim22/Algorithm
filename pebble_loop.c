#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

int check(int p, int q) {
	int checkP = 0;
	if (p == 0) {
		if (q == 1 || q == 2) {
			checkP = 1;
		}
	}
	else if (p == 1) {
		if (q != 1) {
			checkP = 1;
		}
	}
	else if (p == 2) {
		if (q == 0 || q == 1) {
			checkP = 1;
		}
	}
	else if(p == 3) {
		if (q == 1) {
			checkP = 1;
		}
	}

	return checkP;
}
int pebble(int** w,int i, int p,int* cnt) {
	int tmp;
	(*cnt)++;
	if (i = 0) {
		return w[i][p];
	}
	else {
		int max = 0;
		for (int q = 0; q < 4; q++) {
			if (check(p, q)) {
				tmp = pebble(w,i - 1, q,cnt);
				if (tmp > max) {
					max = tmp;
				}
			}
		}
		return max + w[i][p];
	}
}
int pebbleLoop(int** w, int n,int* tmpp,int* cnt) {
	int tmp;
	int max = 0;
	for (int i = 0; i < 4; i++) {
		tmp=pebble(w, n, i,cnt);
		if (tmp > max) {
			max = tmp;
			*tmpp = i;
		}
	}
	return max;
}

int main() {
	int n, maxPattern,cnt=0;

	scanf("%d", &n); //

	int** arr = (int**)malloc(sizeof(int*) * 3); //

	for (int i = 0; i < 3; i++) {
		arr[i] = (int*)malloc(sizeof(int) * n);
	}




	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[i][j]);  //
		}
	}
	printf("\n--------테이블---------\n");
	for (int i = 0; i < 3; i++) {
		printf("\n");
		for (int j = 0; j < n; j++) {
			printf("%d ", arr[i][j]);  
			if (arr[i][j] < 10) {
				printf(" ");
			}
		}
	}

	printf("재귀함수 시 최대값:%d\n",pebbleLoop(arr, n - 1, &maxPattern,&cnt));
	printf("열이 %d 일 때 최대값인 패턴:%d\n", n, maxPattern);
	printf("재귀함수 시 수행횟수:%d", cnt);
}