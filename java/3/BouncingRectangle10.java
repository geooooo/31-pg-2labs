import java.applet.*;
import java.awt.*;
import java.util.Random;


public class BouncingRectangle10 extends Applet implements Runnable {

 	int count = 25;
	int[] dx = new int[count];
	int[] dy = new int[count];
	ColorableRectangle[] rectangle = new ColorableRectangle[count];
	Thread animator;
	volatile boolean pleaseStop;

	public void paint(Graphics g) {
		for (int i = 0; i < this.count; i++) {
			this.rectangle[i].draw(g);
		}
	}

    public void animate() {
    	java.awt.Rectangle bounds = getBounds();
    	for (int i = 0; i < this.count; i++) {
	 		if ((this.rectangle[i].x1 + dx[i] < 0) ||
	 			(this.rectangle[i].x1 + this.rectangle[i].width + dx[i] > bounds.width))
	 		{
	 			dx[i] = -dx[i];
	 		}
	 		if ((this.rectangle[i].y1 + dy[i] < 0) ||
	 			(this.rectangle[i].y1 + this.rectangle[i].height + dy[i] > bounds.height))
	 		{
	 			dy[i] = -dy[i];
	 		}
	 		this.rectangle[i].move(dx[i], dy[i]);
	 		repaint();
	 	}
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
    	Random random = new Random(System.currentTimeMillis());
    	for (int i = 0; i < this.count; i++) {
    		this.dx[i] = random.nextInt(50);
    		this.dy[i] = random.nextInt(20);
    		this.rectangle[i] = new ColorableRectangle(
    			random.nextInt(250), random.nextInt(250),
    			10*(i+1), 10*(i+1),
    			new Color(random.nextInt(255), random.nextInt(255), random.nextInt(255)), new Color(random.nextInt(255), random.nextInt(255), random.nextInt(255)));
    	}
    	animator = new Thread(this);
    	pleaseStop = false;
    	animator.start();
    }

    public void stop() {
    	pleaseStop = true;
    }

}
