/*
    Компилиция и запуск:

    javac test/first/lab.java
    java test.first.Lab 1 2 3
*/


package test.first;



class Lab {
    public static void main(String args[]) {
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }
}
