import java.awt.*;


public class Rectangle {

    protected int x1;
    protected int y1;
    protected int x2;
    protected int y2;

    public Rectangle(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public Rectangle(int x2, int y2) {
        this.x1 = 0;
        this.y1 = 0;
        this.x2 = x2;
        this.y2 = y2;
    }

    public Rectangle() {
        this.x1 = 0;
        this.y1 = 0;
        this.x2 = 0;
        this.y2 = 0;
    }

    public void move(int dx, int dy) {
        this.x1 += dx;
        this.y1 += dy;
        this.x2 += dx;
        this.y2 += dy;
    }

    public Rectangle Union(int x1, int y1, int x2, int y2) {
        int newX1 = Math.min(Math.min(x1, x2), Math.min(this.x1, this.x2));
        int newY1 = Math.min(Math.min(y1, y2), Math.min(this.y1, this.y2));
        int newX2 = Math.max(Math.max(x1, x2), Math.max(this.x1, this.x2));
        int newY2 = Math.max(Math.max(y1, y2), Math.max(this.y1, this.y2));
        return new Rectangle(newX1, newY1, newX2, newY2);
    }

    public void draw(Graphics g) {
        g.drawRect(this.x1,
                   this.y1,
                   this.x2 - this.x1,
                   this.y2 - this.y1);
    }

}

