package facade;

import pets.Dog;
import pets.Cat;

/**
 * 宠物店的接待员 提供给猫/狗洗澡的服务给客户
 * Receptionist at a pet center
 * Providing cat/dog bathing services to customers
 */
public class Receptionist {

    private final Dog dog;

    private final Cat cat;

    /**
     * 构造时 需要对上述Dog和Cat对象进行初始化
     * When constructing, you need to initialize the Dog and Cat objects above.
     */
    public Receptionist() {
        // --- write your code here ---
        dog = new Dog();
        cat = new Cat();

    }

    /**
     * 给客户指定的狗洗澡
     * Bathing the dog specified by the client
     * @param name The name of a dog
     */
    public void dogDoBath(String name) {
        // --- write your code here ---
        dog.bath(name);

    }

    /**
     * 给客户指定的猫洗澡
     * Bathing the cat specified by the client
     * @param name The name of a cat
     */
    public void catDoBath(String name) {
        // --- write your code here ---
        cat.bath(name);

    }

}

// package itf;

// /**
//  * 提供宠物服务的接口
//  * Interface of providing services for pets
//  */
// public interface Pet {
//     /**
//      * 宠物洗浴服务
//      * Pet Bathing Service
//      * @param name A name of a pet
//      */
//     void bath(String name);
// }

// package pets;

// import itf.Pet;

// /**
//  * 宠物的具体类 - 猫
//  * Specific class of Pet - Cat
//  */
// public class Cat implements Pet {

//     @Override
//     public void bath(String name) {
//         System.out.println("Cat: " + name + " -> Taking a bath.");
//     }

// }

// package pets;

// import itf.Pet;

// /**
//  * 宠物的具体类 - 狗
//  * Specific class of Pet - Dog
//  */
// public class Dog implements Pet {

//     @Override
//     public void bath(String name) {
//         System.out.println("Dog: " + name + " -> Taking a bath.");
//     }

// }
