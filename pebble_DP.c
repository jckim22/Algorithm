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
	else if (p == 3) {
		if (q == 1) {
			checkP = 1;
		}
	}

	return checkP;
}
int pebble(int** w, int** peb,int n, int cnt) {
	int tmp,max=0;
	

	for (int p = 0; p < 4; p++) {
		peb[0][p] = w[0][p];
	}
	for (int i = 1; i < n; i++) {
		for (int p = 0; p < 4; p++) {
			for (int q = 0; q < 4; q++) {
				if (check(p, q)) {
					tmp = peb[i - 1][q] + w[i][p];
					if (tmp > max) {
						max = tmp;
					}
				}

			}
			peb[i][p] = max;
		}
	}

	max = peb[n - 1][0];

	for (int i = 1; i < 4; i++) {
		if (peb[n - 1][i] > max) {
			max = peb[n - 1][i];
		}
	}
	return max;
	
}
int main() {
	int n, maxPattern, cnt = 0;

	scanf("%d", &n); //

	int** arr = (int**)malloc(sizeof(int*) * 3); //

	for (int i = 0; i < 3; i++) {
		arr[i] = (int*)malloc(sizeof(int) * n);
	}

	int** peb = (int**)malloc(sizeof(int*) * 3); //

	for (int i = 0; i < 3; i++) {
		peb[i] = (int*)malloc(sizeof(int) * n);
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[i][j]);  //
		}
	}
	printf("\n--------���̺�---------\n");
	for (int i = 0; i < 3; i++) {
		printf("\n");
		for (int j = 0; j < n; j++) {
			printf("%d ", arr[i][j]);
			if (arr[i][j] < 10) {
				printf(" ");
			}
		}
	}

	printf("%d", pebble(arr, peb, n, &cnt));

}