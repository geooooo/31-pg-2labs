import java.awt.*;


public class DrawableRectangle extends Rectangle {

    protected Color outColor;

    public DrawableRectangle(Color outColor, int x1, int y1, int x2, int y2) {
        super(x1, y1, x2, y2);
        this.outColor = outColor;
    }

    public void draw(Graphics g) {
        g.setColor(outColor);
        super.draw(g);
    }
}
