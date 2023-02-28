import java.util.Scanner;

class armStrong {
    public static void main(String args[]) {
        int c = 0, a, temp;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number:");
        int n = sc.nextInt();
        temp = n;
        while (n > 0) {
            a = n % 10;
            n = n / 10;
            c = c + (a * a * a);
        }
        if (temp == c)
            System.out.println(c + "is an armstrong number");
        else
            System.out.println(c + "is not an armstrong number");
        sc.close();
    }
}