import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

//아이디어:
// 상하좌우 4번 반복하는 depth가 5인 백트랙킹을 진행
// 1. 방향 가장 가까운 블록을 방향으로 이동
//-> -> : 0이 아니면 멈추고 숫자를 확인
// -> 조건1: 숫자가 다르면 그 앞에서 멈춰야함
// -> 조건2: 숫자가 같으면 합쳐짐
// -> 조건3: 이미 한번 합쳐진 블록이라면 결합 불가
//자료구조:
//합쳐진 블록의 인덱스를 갖고 있을 리스트
//시간복잡도:
//시간이 매우 짧기 때문에 이동하는 시간을 거의 없는 것으로 만들어야함

public class Easy2048 {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static ArrayList<int[]> fusionBlock;
    static ArrayList<int[]> blockSeq;
    static int[][] matrix;
    static int n;
    static int maxBlock = -1;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        StringTokenizer st;
        matrix = new int[n][n];
        fusionBlock = new ArrayList<>();
        blockSeq = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        back(0);
        System.out.println(maxBlock);
    }

    public static void back(int depth) {
        if (depth == 5) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] != 0) {
                        if (maxBlock < matrix[i][j]) {
                            maxBlock = matrix[i][j];
                        }
                    }
                }
            }
            return;
        }
        for (int i = 0; i < 4; i++) {
            blockSeq = new ArrayList<>();
            if (i == 0) {
                for (int j = 0; j < n; j++) {
                    for (int h = n - 1; h >= 0; h--) {
                        if (matrix[j][h] != 0) {
                            blockSeq.add(new int[]{j, h});
                        }
                    }
                }
            } else if (i == 1) {
                for (int j = 0; j < n; j++) {
                    for (int h = 0; h < n; h++) {
                        if (matrix[j][h] != 0) {
                            blockSeq.add(new int[]{j, h});
                        }
                    }
                }
            } else if (i == 2) {
                for (int j = 0; j < n; j++) {
                    for (int h = n - 1; h >= 0; h--) {
                        if (matrix[h][j] != 0) {
                            blockSeq.add(new int[]{h, j});
                        }
                    }
                }
            } else if (i == 3) {
                for (int j = 0; j < n; j++) {
                    for (int h = 0; h < n; h++) {
                        if (matrix[h][j] != 0) {
                            blockSeq.add(new int[]{h, j});
                        }
                    }
                }
            }
            int[][] matrixCopy = new int[n][n];
            for (int z = 0; z < n; z++) {
                for (int c = 0; c < n; c++) {
                    matrixCopy[z][c] = matrix[z][c];
                }
            }
            fusionBlock = new ArrayList<>();
            for (int j = 0; j < blockSeq.size(); j++) {
                int[] cur = blockSeq.get(j);
                move(cur[0], cur[1], i, cur[0] + dx[i], cur[1] + dy[i], cur[0], cur[1]);
            }
//            for (int[] a : matrix) {
//                System.out.println(Arrays.toString(a));
//            }
//            System.out.println();
            back(depth + 1);
            matrix = matrixCopy;
        }
    }

    public static void move(int x, int y, int vector, int nx, int ny, int bx, int by) {
        if (ny >= n || ny < 0 || nx >= n || nx < 0) {
            return;
        }
        //끝인지 판별
        boolean check = false;
        if (vector == 0) {
            if (ny == n - 1) {
                check = true;
            }
        } else if (vector == 1) {
            if (ny == 0) {
                check = true;
            }
        } else if (vector == 2) {
            if (nx == n - 1) {
                check = true;
            }
        } else if (vector == 3) {
            if (nx == 0) {
                check = true;
            }
        }
        if (matrix[nx][ny] != 0 || check) {
            if (matrix[nx][ny] == 0) {
                matrix[nx][ny] = matrix[x][y];
                matrix[x][y] = 0;
                return;
            }
            //결합
//            for (int[] arr : fusionBlock) {
//                System.out.println(Arrays.toString(arr));
//            }
            if (matrix[nx][ny] == matrix[x][y] && !(containsArray(fusionBlock, new int[]{nx, ny}))) {
                matrix[nx][ny] *= 2;
                matrix[bx][by] = 0;
                fusionBlock.add(new int[]{nx, ny});
            } else {
                matrix[bx][by] = matrix[x][y];
                if (bx == x && by == y) {
                    return;
                }
            }
            matrix[x][y] = 0;
            return;

        }
        move(x, y, vector, nx + dx[vector], ny + dy[vector], nx, ny);
    }

    private static boolean containsArray(ArrayList<int[]> list, int[] array) {
        for (int[] element : list) {
            if (Arrays.equals(element, array)) {
                return true;
            }
        }
        return false;
    }
}
