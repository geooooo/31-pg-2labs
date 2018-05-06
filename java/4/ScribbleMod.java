import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;


public class ScribbleMod extends Applet {

	int last_x;
	int last_y;
	Color color;

	public void init() {

		this.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				// right button press
				if (e.getModifiers() == 4) {
					Random random = new Random();
					color = new Color(random.nextInt(255),
									  random.nextInt(255),
									  random.nextInt(255));
				} else {
					last_x = e.getX(); 
					last_y = e.getY();
				}
			}
		}); 

		this.addMouseMotionListener(new MouseMotionAdapter() {
			public void mouseDragged(MouseEvent e) {
				// left button press
				if (e.getModifiers() == 16) {
					Graphics g = getGraphics();
					int x = e.getX();
					int y = e.getY();
					g.setColor(color);
					g.drawRect(last_x,
						       last_y, 
							   Math.abs(x - last_x + 5),
							   Math.abs(y - last_y + 5));
					last_x = x;
					last_y = y;
				}
			}
		});

		Button b = new Button("Clear");

		b.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Graphics g = getGraphics(); 
				g.setColor(getBackground());
				g.fillRect(0, 0, getSize().width, getSize().height);
			}
		});

		this.add(b);
	}

}