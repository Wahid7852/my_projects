import java.util.Scanner;

class minNum {
    public static void main(String args[]) {
        int a, b;
        System.out.println("Enter Two numbers\n");
        Scanner obj = new Scanner(System.in);
        a = obj.nextInt();
        b = obj.nextInt();
        System.out.println("The smallest values is " + Math.min(a, b));
        obj.close();
    }
}