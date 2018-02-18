package test.second;



class Lab {
    private static final int MAX_NUMBER = 100;

    public static void main(String args[]) {
        for (int i = 1; i <= Lab.MAX_NUMBER; i++) {
            if ((i % 5 == 0) && (i % 7 == 0)) {
                System.out.println("fizzbuzz");
            } else if (i % 5 == 0) {
                System.out.println("fizz");
            } else if (i % 7 == 0) {
                System.out.println("buzz");
            } else {
                System.out.println(i);
            }
        }
    }
}
