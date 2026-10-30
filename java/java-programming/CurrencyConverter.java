import java.util.Scanner;

public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Fixed rate for testing: 1 USD = 83.50 INR
        double usdToInr = 83.50;

        System.out.println("--- Simple Currency Converter ---");
        System.out.print("Enter amount in USD: ");
        double amount = sc.nextDouble();

        double converted = amount * usdToInr;

        System.out.printf("%.2f USD is equal to %.2f INR%n", amount, converted);

        sc.close();
    }
}