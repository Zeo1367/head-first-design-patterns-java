package chapter_01_strategy.duck_example.model;

import chapter_01_strategy.duck_example.behavior.fly.FlyWithWings;
import chapter_01_strategy.duck_example.behavior.quack.Quack;

public class MallardDuck extends Duck {

    public MallardDuck() {
        flyBehavior = new FlyWithWings();
        quackBehavior = new Quack();
    }

    public void display() {
        System.out.println("I am a Mallard Duck");
    }
}