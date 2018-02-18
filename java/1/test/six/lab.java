package test.six;



class Lab {
    private static int[] primes(int number) {
        int[] sieve = new int[number];
        for (int i = 0; i < number; i++) {
            sieve[i] = i;
        }
        sieve[1] = 0;
        for (int i : sieve) {
            if (i > 1) {
                for (int j = i + i; j < number; j += i) {
                    sieve[j] = 0;
                }
            }
        }
        return sieve;
    }

    public static void main(String args[]) {
        int[] result = Lab.primes(Integer.parseInt(args[0]));
        for (int i : result) {
            System.out.print(i);
            System.out.print(" ");
        }
        System.out.println();
    }
}
