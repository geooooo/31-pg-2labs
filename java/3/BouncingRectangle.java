import java.applet.*;
import java.awt.*; 
 
 
public class BouncingRectangle extends Applet implements Runnable {
 
	int dx = 10;
	int dy = 4;
	ColorableRectangle rectangle = new ColorableRectangle(50, 50, Color.blue, Color.yellow);
	Thread animator;     
	volatile boolean pleaseStop; 

	public void paint(Graphics g) {
		this.rectangle.draw(g);
	} 
 
    public void animate() {
    	java.awt.Rectangle bounds = getBounds();
 		if ((this.rectangle.x1 + dx < 0) ||
 			(this.rectangle.x1 + this.rectangle.width + dx > bounds.width))
 		{ 
 			dx = -dx;
 		}
 		if ((this.rectangle.y1 + dy < 0) ||
 			(this.rectangle.y1 + this.rectangle.height + dy > bounds.height))
 		{
 			dy = -dy; 
 		}
 		this.rectangle.move(dx, dy);
 		repaint();
 	} 
	public void run() {
		while(!pleaseStop) {
			animate();
			try {
				Thread.sleep(10);
			} catch(InterruptedException e) {} 
		} 
	} 
 
    public void start() {
    	animator = new Thread(this);
    	pleaseStop = false; 
    	animator.start();
    } 

    public void stop() {
    	pleaseStop = true;
    }

} 