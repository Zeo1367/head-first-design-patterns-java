package payment_method.model;

import payment_method.strategies.CreditCardPaymentStrategy;

public class CreditCardPayment extends PaymentProcessor {
    public CreditCardPayment() {
        ps = new CreditCardPaymentStrategy();
    }

    @Override
    public void startPayment() {
        System.out.println("Starting payment using credit card!");
    }
}
