package test.four;



class Lab {
    private static long fib(int number) {
        long prev = 0;
        long cur = 1;
        for (int i = 0; i < number; i++) {
            long tmp = prev;
            prev = cur;
            cur += tmp;
        }
        return cur;
    }

    public static void main(String args[]) {
        System.out.println(Lab.fib(Integer.parseInt(args[0])));
    }
}
