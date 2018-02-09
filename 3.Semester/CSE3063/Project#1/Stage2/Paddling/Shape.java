
public class Shape {

	//Coordinates of shapes
	protected int x;
	protected int y;
		
	public Shape(){
		super();
	}
	
	public Shape(int x, int y){
		this.x = x;
		this.y = y;
	}

	@Override
	public String toString() {
		return "Shape [x=" + x + ", y=" + y + "]";
	}
	
}
