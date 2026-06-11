package chapter_01_strategy.duck_example;

import chapter_01_strategy.duck_example.behavior.fly.FlyRocketPowered;
import chapter_01_strategy.duck_example.model.Duck;
import chapter_01_strategy.duck_example.model.MallardDuck;
import chapter_01_strategy.duck_example.model.RubberDuck;
import chapter_01_strategy.duck_example.model.WoodenDuck;

public class ExecuteDuck {
    public static void main(String[] args) {
        System.out.println("-----------------------------------");

        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.performFly();
        mallard.performQuack();

        System.out.println("-----------------------------------");

        Duck rubber = new RubberDuck();
        rubber.display();
        rubber.performFly();
        rubber.performQuack();

        System.out.println("-----------------------------------");

        Duck wooden = new WoodenDuck();
        wooden.display();
        wooden.performFly();
        wooden.performQuack();

        System.out.println("-----------------------------------");

        // Change behavior at runtime
        mallard.setFlyBehavior(new FlyRocketPowered());
        mallard.performFly();

        System.out.println("-----------------------------------");
    }
}