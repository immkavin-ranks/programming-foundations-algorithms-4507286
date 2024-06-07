
public class Gcd {

    private static int calculateGcd(int a, int b) {
        while (b != 0) {
            int temp = a;
            a = b;
            b = temp % a;
        }
        return a;
    }

    public static void main(String[] args) {
        System.err.println(calculateGcd(8, 20));
    }
}
