package test.three;



class Lab {
    public static void main(String args[]) {
        for (int i = args.length - 1; i >= 0; i--) {
            System.out.print(new StringBuilder(args[i]).reverse() + " ");
        }
        System.out.println();
    }
}
