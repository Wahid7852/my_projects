import java.util.Scanner;

class binaryToDecimal {
    public static void main(String args[]) {
        int a, b, c = 0, d = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number:");
        int n = sc.nextInt();
        while (n > 0) {
            a = n % 10;
            n = n / 10;
            b = (int) Math.pow(2, d);
            c = c + (a * b);
            d++;
        }
        System.out.println("The decimal value is " + c);
        sc.close();
    }
}
