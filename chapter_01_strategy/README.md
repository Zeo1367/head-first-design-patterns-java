# Strategy Pattern

## What is Strategy Pattern?

The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

In simple words:
**Strategy Pattern = Change behavior at runtime using composition instead of inheritance.**

---

## Real Life Example

Think about Google Maps:
You can choose different navigation strategies:

* Car
* Bike
* Walking
* Public Transport

The app changes the navigation behavior based on the strategy you choose.

---

## When to Use

Use Strategy Pattern when:

* You have many similar classes that only differ in behavior
* You want to change behavior at runtime
* You want to avoid too many if-else conditions
* You want to follow "Favor composition over inheritance"

---

## Structure

Strategy Pattern has:

1. Context (chapter_01_strategy.duck_example.ExecuteDuck class)
2. Strategy Interface
3. Concrete Strategies

```
Context → uses → Strategy Interface → implemented by → Concrete Strategies
```

---

## Real World Examples in Software

| Example        | Strategy                   |
| -------------- | -------------------------- |
| Payment App    | Credit Card / UPI / PayPal |
| Navigation     | Car / Bike / Walk          |
| Sorting        | QuickSort / MergeSort      |
| Compression    | ZIP / RAR                  |
| Authentication | Google / Facebook / Email  |

---

## Key Principle

**Favor Composition Over Inheritance**

Instead of writing:

```
class Duck extends FlyDuck
class Duck extends NoFlyDuck
```

We write:

```
Duck has-a FlyBehavior
Duck has-a QuackBehavior
```

---

## What You Will Find in This Folder

* problem.md → What problem we are solving
* solution.md → How Strategy Pattern solves it
* code → Implementation
* real_world_example → Payment example

```
```
