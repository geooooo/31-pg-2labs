class Rectangle {


    protected int x1;
    protected int x2;
    protected int y1;
    protected int y2;


    public Rectangle(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }


    public Rectangle(int width, int height) {
        this.x1 = this.y2 = 0;
        this.y1 = height;
        this.x2 = width;
    }


    public Rectangle() {
        this.x1 = this.y1 = 0;
        this.x2 = this.y2 = 0;
    }


    public void rectPrint() {
        System.out.format("(%d;%d) (%d;%d)\n", this.x1, this.y1, this.x2, this.y2);
    }


    public void move(int dx, int dy) {
        this.x1 += dx;
        this.x2 += dx;
        this.y1 += dy;
        this.y2 += dy;
    }


    public Rectangle union(final Rectangle other) {
        int newX1 = Math.min(this.x1, other.x1);
        int newX2 = Math.max(this.x2, other.x2);
        int newY1 = Math.max(this.y1, other.y1);
        int newY2 = Math.min(this.y2, other.y2);
        return new Rectangle(newX1, newY1, newX2, newY2);
    }

}
