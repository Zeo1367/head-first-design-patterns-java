package chapter_01_strategy.duck_example.behavior.quack;

public class Quack implements QuackBehavior {
    public void quack() {
        System.out.println("Quack");
    }
}