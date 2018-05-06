import java.awt.*;


public class ColoredRectangle extends DrawableRectangle {

    private Color inColor;

    public ColoredRectangle(Color inColor, Color outColor,
                       int x1, int y1, int x2, int y2) {
        super(outColor, x1, y1, x2, y2);
        this.inColor = inColor;
    }

    public void draw(Graphics g) {
        super.draw(g);
        g.setColor(inColor);
        g.fillRect(this.x1 + 1,
                   this.y1 + 1,
                   this.x2 - this.x1 - 1,
                   this.y2 - this.y1 - 1);
    }
}
