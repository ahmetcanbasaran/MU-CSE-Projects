//This class have a no-arg. constructor and another 
//type constructor which can be specified as you wish.

class Rectangle {
	
	
	//Define the width and height with default value 1
	double width = 1;
	double height = 1;
	
	
	//Define perimeter and area variables. They can be defined public or private.
	public double perimeter;
	public double area;
	
	
	//Create a rectangle object with default values 
	public Rectangle(){
	
	}
	
	
	//Create a rectangle object whic has changable width and height values
	public Rectangle (double value1, double value2){
				
		width = value1;
		height = value2;
		
	}
	
	
	/*Create a public method which calculates 
	**area of the rectangle and accessable from main class*/
	public double getArea() {
		
		double area = width * height;
		
		return area;
		
	}
	
	
	/*Create a public method which calculates perimeter
	**of the rectangle and accessable from main class*/
	public double getPerimeter() {
		
		double perimeter = 2 * (width + height);
		
		return perimeter;
		
		}
		
		
	//This method support to print the object with it's values
	public String toString(){
		
		String phrase;
		
		phrase = "\t" + "Rectangle's width: " + width + "\n" +
						"\t" + "Rectangle's height: " + height;
		
		return phrase;
		
	}
	
}
