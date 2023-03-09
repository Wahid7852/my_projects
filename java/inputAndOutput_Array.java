import java.util.Scanner;

public class inputAndOutput_Array {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            int[] numbers = new int[10];
            int i;

            for (i = 0; i < numbers.length; i++) {
                System.out.print("Enter number: ");
                numbers[i] = input.nextInt();
            }

            for (i = 0; i < numbers.length; i++) {
                System.out.println("Number " + (i + 1) + " is " + numbers[i]);
            }
        }
    }
}
