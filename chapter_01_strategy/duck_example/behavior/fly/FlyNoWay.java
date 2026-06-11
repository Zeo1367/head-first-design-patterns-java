package chapter_01_strategy.duck_example.behavior.fly;

public class FlyNoWay implements FlyBehavior {
    public void fly() {
        System.out.println("I cannot fly.");
    }
}
