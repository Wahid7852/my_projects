class upperMul {
    static void sum(int mat[][], int r, int c) {
        int i, j;
        int upper_sum = 0;
        int lower_sum = 0;

        for (i = 0; i < r; i++)
            for (j = 0; j < c; j++) {
                if (i <= j) {
                    upper_sum += mat[i][j];
                }
            }

        System.out.println("Upper sum is " + upper_sum);

        for (i = 0; i < r; i++)
            for (j = 0; j < c; j++) {
                if (j <= i) {
                    lower_sum += mat[i][j];
                }
            }

        System.out.print("Lower sum is " + lower_sum);
    }

    public static void main(String[] args) {
        int r = 3;
        int c = 3;

        int mat[][] = { { 6, 5, 4 }, { 1, 2, 5 }, { 7, 9, 7 } };
        sum(mat, r, c);
    }
}
