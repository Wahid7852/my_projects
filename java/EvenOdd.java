import java.util.Scanner;

public class EvenOdd {
    public static void main(String[] args) {
        Scanner r = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = r.nextInt();
        if (num % 2 == 0)
            System.out.println(num + " is even");
        else
            System.out.println(num + " is odd");
        r.close();
    }
}