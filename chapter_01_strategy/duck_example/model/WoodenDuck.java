package chapter_01_strategy.duck_example.model;

import chapter_01_strategy.duck_example.behavior.fly.FlyNoWay;
import chapter_01_strategy.duck_example.behavior.quack.MuteQuack;

public class WoodenDuck extends Duck {
    public WoodenDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new MuteQuack();
    }

    @Override
    public void display() {
        System.out.println("I am a Wooden Duck");
    }
}
