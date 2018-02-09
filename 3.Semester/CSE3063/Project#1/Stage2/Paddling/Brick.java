
public class Brick extends Shape{

	String color = "DEFAULT";
	
	public Brick(){
		super();
	}
	
	public Brick(int x, int y){
		
		super(x,y);
		
	}
	
	public Brick(String color, int x, int y){
		
		super(x,y);
		
		this.color = color;
		
	}
	
	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	
	@Override
	public String toString() {
		return "Brick [color=" + color + ", x=" + x + ", y=" + y + "]";
	}
	
	
	
}
