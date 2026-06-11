package chapter_01_strategy.payment_method.strategies;

public class UpiPaymentStrategy implements PaymentStrategy {

    @Override
    public void pay(double amount) {
        System.out.println("Payed " + amount + " using UPI!");
    }
}
