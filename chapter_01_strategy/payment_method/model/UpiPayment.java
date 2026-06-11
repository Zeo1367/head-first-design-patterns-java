package chapter_01_strategy.payment_method.model;

import chapter_01_strategy.payment_method.strategies.UpiPaymentStrategy;

public class UpiPayment extends PaymentProcessor {
    public UpiPayment() {
        ps = new UpiPaymentStrategy();
    }

    @Override
    public void startPayment() {
        System.out.println("Starting payment using UPI!");
    }
}
