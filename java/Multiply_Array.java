//create 2 dimensional array and multiply them 

import java.util.Scanner;

public class Multiply_Array {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            int[][] numbers = new int[10][10];
            int i, j;

            for (i = 0; i < numbers.length; i++) {
                for (j = 0; j < numbers[i].length; j++) {
                    System.out.print("Enter number: ");
                    numbers[i][j] = input.nextInt();
                }
            }

            for (i = 0; i < numbers.length; i++) {
                for (j = 0; j < numbers[i].length; j++) {
                    System.out.println("Number " + (i + 1) + " is " + numbers[i][j]);
                }
            }
        }
    }
}