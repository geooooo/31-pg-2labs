import java.awt.*;


class ColorableRectangle extends ColoredRectangle {

	int width;
	int height;

	public ColorableRectangle(int width, int height,
							  Color outColor, Color inColor) {
		this.width = width;
		this.height = height;
		this.outColor = outColor;
		this.inColor  = inColor;
		this.x1 = this.y1 = 0;
	}

	public ColorableRectangle(int x1, int y1, int width, int height,
							  Color outColor, Color inColor) {
		this(width, height, outColor, inColor);
		this.x1 = x1;
		this.y1 = y1;
	}

	@Override
	public void draw(Graphics g) {
		g.setColor(this.inColor);
		g.fillRect(this.x1, this.y1, this.width, this.height);
		g.setColor(this.outColor);
		g.drawRect(this.x1, this.y1, this.width, this.height);
	}

}