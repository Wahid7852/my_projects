class CI {
    public static void main(String args[]) {
        double principal = 100, rate = 10, time = 3;
        double CI = principal * (Math.pow((1 + rate / 100), time));
        System.out.println("Compound Interest is " + CI);
    }
}