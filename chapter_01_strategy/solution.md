# Solution – Strategy Pattern

## Idea

Instead of putting fly() and quack() inside Duck class,
we separate the behaviors into different classes.

This is called:
**Encapsulate what varies.**

The things that vary are:

* Flying behavior
* Quacking behavior

So we create:

* FlyBehavior interface
* QuackBehavior interface

---

## Structure

```
Duck (Context)
  |
  | has-a
  ↓
FlyBehavior (Interface)
  ├── FlyWithWings
  ├── FlyNoWay

QuackBehavior (Interface)
  ├── Quack
  ├── Squeak
  ├── MuteQuack
```

Duck does not implement flying itself.
Duck **delegates** flying to FlyBehavior object.

---

## How It Works

```
duck.setFlyBehavior(new FlyWithWings())
duck.performFly()
```

We can change behavior at runtime:

```
duck.setFlyBehavior(new FlyNoWay())
```

This is the biggest advantage of Strategy Pattern.

---

## Benefits

| Benefit                  | Explanation          |
| ------------------------ | -------------------- |
| No code duplication      | Behaviors are reused |
| Easy to add new behavior | Just add new class   |
| Runtime behavior change  | Yes                  |
| Follows SOLID principles | Yes                  |
| Flexible design          | Yes                  |

---

## Design Principle Used

**Favor Composition Over Inheritance**

Instead of:

```
Duck extends Flyable
```

We use:

```
Duck has a FlyBehavior
```

---

## Strategy Pattern Summary

| Component          | Role                       |
| ------------------ | -------------------------- |
| Context            | Duck                       |
| Strategy Interface | FlyBehavior, QuackBehavior |
| Concrete Strategy  | FlyWithWings, Squeak, etc  |

---

## Real World Example – Payment System

Context: PaymentApp
Strategy Interface: PaymentStrategy
Concrete Strategies:

* CreditCardPayment
* UpiPayment
* PaypalPayment

User selects payment method → Strategy changes.

---

## One Line Definition (Interview)

**Strategy Pattern allows selecting an algorithm’s behavior at runtime by encapsulating it into separate classes.**

| Part               | In Our Example                        |
| ------------------ | ------------------------------------- |
| Context            | Duck                                  |
| Strategy Interface | FlyBehavior, QuackBehavior            |
| Concrete Strategy  | FlyWithWings, FlyNoWay, Quack, Squeak |
| Runtime Change     | set_fly_behavior()                    |


```
```
