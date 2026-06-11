package duck_example.model;

import duck_example.behavior.fly.FlyNoWay;
import duck_example.behavior.quack.Squeak;

public class RubberDuck extends Duck {

    public RubberDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new Squeak();
    }

    public void display() {
        System.out.println("I am a Rubber Duck");
    }
}