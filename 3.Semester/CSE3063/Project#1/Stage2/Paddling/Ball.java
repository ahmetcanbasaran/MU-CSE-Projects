
public class Ball extends Shape{

	boolean willStick = false;
	boolean canDestroy = false;
	boolean canExplode = false;
	boolean canMove = true;

	public Ball(){
		super();
	}
	
	public Ball(int x, int y){
		
		super(x, y);
		
	}

	@Override
	public String toString() {
		return "Ball [x=" + x + ", y=" + y + "]";
	}
	
	
	
}
