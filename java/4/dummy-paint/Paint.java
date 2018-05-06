import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;


public class Paint extends Applet {

    private Button button2 = new Button("Цветной");
    private Button button3 = new Button("Закрашенный");
    private Rectangle[] rectangles = new Rectangle[1000];
    private int ri = 0;
    private int ii;
    private int lastX;
    private int lastY;

    public void init() {

        this.addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                if ((e.getModifiers() & MouseEvent.BUTTON1_MASK) != 0) {
                    lastX = e.getX();
                    lastY = e.getY();
                    for (int i = ri - 1; i >= 0; i--) {
                        if ((rectangles[i].x1 < lastX) &&
                            (rectangles[i].y1 < lastY) &
                            (rectangles[i].x2 > lastX) &&
                            (rectangles[i].y2 > lastY))
                        {
                            ii = i;
                            break;
                        }
                    }
                }
            }
        });

        this.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
                if ((e.getModifiers() & MouseEvent.BUTTON1_MASK) != 0) {
                    Graphics g = getGraphics();
                    int x = e.getX();
                    int y = e.getY();
                    g.setColor(getBackground());
                    g.fillRect(0, 0, getSize().width, getSize().height);
                    rectangles[ii].move(x - lastX, y - lastY);
                    for (int i = 0; i < ri; i++) {
                        rectangles[i].draw(g);
                    }
                    lastX = x;
                    lastY = y;
                }
            }
        });

        button2.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    Graphics g = getGraphics();
                    Random random = new Random();
                    Color color = new Color(random.nextFloat(),
                                            random.nextFloat(),
                                            random.nextFloat());
                    int x1 = 100 + random.nextInt(500);
                    int y1 = 100 + random.nextInt(500);
                    int w = random.nextInt(100);
                    int h = random.nextInt(100);
                    DrawableRectangle r = new DrawableRectangle(color, x1, y1, x1 + w, y1 + h);
                    if (ri <= rectangles.length) {
                        rectangles[ri++] = r;
                        r.draw(g);
                    }
                }
        });

        button3.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                Graphics g = getGraphics();
                Random random = new Random();
                Color color1 = new Color(random.nextFloat(),
                                         random.nextFloat(),
                                         random.nextFloat());
                Color color2 = new Color(random.nextFloat(),
                                         random.nextFloat(),
                                         random.nextFloat());
                int x1 = 100 + random.nextInt(500);
                int y1 = 100 + random.nextInt(500);
                int w = random.nextInt(100);
                int h = random.nextInt(100);
                ColoredRectangle r = new ColoredRectangle(color1, color2, x1, y1, x1 + w, y1 + h);
                if (ri <= rectangles.length) {
                    rectangles[ri++] = r;
                    r.draw(g);
                }
            }
        });

        this.add(button2);
        this.add(button3);
    }

}
