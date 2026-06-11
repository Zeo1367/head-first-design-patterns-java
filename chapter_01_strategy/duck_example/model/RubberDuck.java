package chapter_01_strategy.duck_example.model;

import chapter_01_strategy.duck_example.behavior.fly.FlyNoWay;
import chapter_01_strategy.duck_example.behavior.quack.Squeak;

public class RubberDuck extends Duck {

    public RubberDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new Squeak();
    }

    public void display() {
        System.out.println("I am a Rubber Duck");
    }
}