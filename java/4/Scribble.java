import java.applet.*;
import java.awt.*;
import java.awt.event.*;


public class Scribble extends Applet {

	int last_x;
	int last_y;

	public void init() {

		this.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				last_x = e.getX(); last_y = e.getY();
			}
		}); 

		this.addMouseMotionListener(new MouseMotionAdapter() {
			public void mouseDragged(MouseEvent e) {
				Graphics g = getGraphics();
				int x = e.getX();
				int y= e.getY();
				g.setColor(Color.black);
				g.drawLine(last_x, last_y, x, y);
				last_x = x; last_y = y;
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