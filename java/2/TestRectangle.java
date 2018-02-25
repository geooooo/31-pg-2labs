class TestRectangle {

    public static void main(String args[]) {
        System.out.println("Конструктор:");
        new Rectangle().rectPrint();
        new Rectangle(1, 2, 3, 4).rectPrint();
        new Rectangle(10, 20).rectPrint();
        System.out.println();

        System.out.println("Метод move:");
        Rectangle r = new Rectangle(10, 10, 30, 20);
        r.rectPrint();
        r.move(10, 0);
        r.rectPrint();
        r.move(-10, 10);
        r.rectPrint();
        r.move(0, -10);
        r.rectPrint();
        System.out.println();

        System.out.println("Метод union:");
        /*
            #==
        */
        new Rectangle(1, 1).union(new Rectangle(1, 1, 3, 0)).rectPrint();
        /*
            Тоже самое, что и предыдущее, только фигуры наоборот
        */
        new Rectangle(1, 1, 3, 0).union(new Rectangle(1, 1)).rectPrint();
        /*
            --###
            -----
            ###--
        */
        new Rectangle(3, 1).union(new Rectangle(3, 3, 5, 3)).rectPrint();
        /*
            Тоже самое, что и предыдущее, только фигуры наоборот
        */
        new Rectangle(3, 3, 5, 3).union(new Rectangle(3, 1)).rectPrint();
        /*
            -###
            -###
            ----

            Прямоугольники совпадают
        */
        new Rectangle(2, 3, 4, 2).union(new Rectangle(2, 3, 4, 2)).rectPrint();
        /*
            Тоже самое, что и предыдущее, только фигуры наоборот
        */
        new Rectangle(2, 3, 4, 2).union(new Rectangle(2, 3, 4, 2)).rectPrint();
        /*
            --##-------
            --##--#####
            --##-------
            --##-------
            -----------
        */
        new Rectangle(3, 5, 4, 2).union(new Rectangle(7, 4, 11, 7)).rectPrint();
        /*
            Тоже самое, что и предыдущее, только фигуры наоборот
        */
        new Rectangle(7, 4, 11, 7).union(new Rectangle(3, 5, 4, 2)).rectPrint();
    }

}
