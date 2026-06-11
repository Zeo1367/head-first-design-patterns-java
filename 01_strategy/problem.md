# Problem – Why Do We Need Strategy Pattern?

## Duck Example

Suppose we are building a Duck Game.

We have different types of ducks:

* Mallard Duck (flies + quacks)
* Rubber Duck (does not fly + squeaks)
* Wooden Duck (does not fly + does not quack)

### Initial Design (Using Inheritance)

```
Duck
 ├── duck_example.model.MallardDuck
 ├── duck_example.model.RubberDuck
 └── duck_example.model.WoodenDuck
```

All ducks inherit from Duck class.

Duck class has:

* fly()
* quack()
* swim()

### The Problem

Not all ducks fly and quack the same way.

| Duck    | Fly    | Quack  |
| ------- | ------ | ------ |
| Mallard | Fly    | Quack  |
| Rubber  | No Fly | Squeak |
| Wooden  | No Fly | Silent |

If we put fly() and quack() in base class:

* Rubber duck will fly ❌
* Wooden duck will quack ❌

If we override methods:

* Code duplication
* Hard to maintain
* Changes in fly behavior require changing many classes
* Cannot change behavior at runtime

### duck_example Main Problems:

1. Code duplication
2. Hard to add new behavior
3. Hard to change behavior at runtime
4. Too many overrides
5. Violates good design principles

### Bad Design Example

```
public class Duck {

    public void fly() {
        System.out.println("Flying");
    }

    public void quack() {
        System.out.println("Quack");
    }
}

public class RubberDuck extends Duck {

    @Override
    public void fly() {
        System.out.println("I cannot fly");
    }

    @Override
    public void quack() {
        System.out.println("Squeak");
    }
}
```

This design is not flexible.

We need a better design.

```
```
