import java.util.Arrays;
import java.util.concurrent.SynchronousQueue;
import java.util.stream.Collectors;

class Foo {
    private int a = 5;
    int c;

    public Foo(int arg) {
        a = arg;
        this.c = 1;
    }

    public Foo() {
    }

    public int getA() {
        // this --> the object that it is called with
        // This 'this' here is not required strictly but just for illustration
        return this.a;
    }
}

public class HelloWorld {
    static void printFoos(Foo[] theFoos) {
        // Since it is a static method, it has no notion of 'this'
        // Print out the 'a' values of all the foos in theFoos
        // You write this !
        for (int i = 0; i < theFoos.length; ++i) {
            String toPrint = theFoos[i] == null ? "null" : Integer.toString(theFoos[i].getA());
            System.out.println("CheenCheen " + toPrint);
        }
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            for (int i = 0; i < args.length; ++i) {
                System.out.println("The thing is " + args[i]);
            }
        }
        Foo monkey = new Foo(1);
        Foo smellyMonkey = new Foo(3);
        Foo badMonkey = new Foo();
        System.out.println("The monkey foo is " + monkey.getA());
        System.out.println("The smellyMonkey foo is " + smellyMonkey.getA());
        System.out.println("The badMonkey foo is " + badMonkey.getA());

        Foo[] awesomeArray = new Foo[10];
        printFoos(awesomeArray);
        for (int i = 0; i < awesomeArray.length; ++i) {
            awesomeArray[i] = new Foo(i * 2);
        }
        printFoos(awesomeArray);
    }
}
