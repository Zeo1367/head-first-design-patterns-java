package payment_method.model;

import payment_method.strategies.PaymentStrategy;

public abstract class PaymentProcessor {
    PaymentStrategy ps;

    public abstract void startPayment();

    public void pay(double amount) {
        ps.pay(amount);
    };
}
