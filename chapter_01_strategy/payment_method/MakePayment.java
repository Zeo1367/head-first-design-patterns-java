package chapter_01_strategy.payment_method;

import chapter_01_strategy.payment_method.model.CreditCardPayment;
import chapter_01_strategy.payment_method.model.PaymentProcessor;
import chapter_01_strategy.payment_method.model.UpiPayment;

public class MakePayment {
    public static void main(String[] args) {
        System.out.println("-----------------------------------");

        PaymentProcessor upiPaymentProcessor = new UpiPayment();
        upiPaymentProcessor.startPayment();
        upiPaymentProcessor.pay(50.20);

        System.out.println("-----------------------------------");

        PaymentProcessor ccPaymentProcessor = new CreditCardPayment();
        ccPaymentProcessor.startPayment();
        ccPaymentProcessor.pay(800.44);

        System.out.println("-----------------------------------");
    }
}
