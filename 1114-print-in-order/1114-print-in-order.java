class Foo {

    private volatile int flag;
    
    public Foo() {
        
        flag = 1;
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        for(;;) {
            if (flag==1) {
                printFirst.run();
                flag = 2;
                break;
            }
        }
        
        // // printFirst.run() outputs "first". Do not change or remove this line.
        // printFirst.run();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        for(;;) {
            if (flag == 2) {
                printSecond.run();
                flag = 3;
                break;
            }
        }
        
        // // printSecond.run() outputs "second". Do not change or remove this line.
        // printSecond.run();
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        for(;;) {
            if (flag == 3) {
                printThird.run();
                flag = 1;
                break;
            }
        }
        
        // // printThird.run() outputs "third". Do not change or remove this line.
        // printThird.run();
    }
}