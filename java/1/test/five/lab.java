package test.five;



class Lab {
    private static long fac(int number) {
        if (number == 1) {
            return 1;
        }
        return number * Lab.fac(number - 1);
    }

    public static void main(String args[]) {
        System.out.println(Lab.fac(Integer.parseInt(args[0])));
    }
}
