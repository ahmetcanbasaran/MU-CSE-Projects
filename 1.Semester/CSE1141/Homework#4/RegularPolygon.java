/*This class creates regular polygons with or without using specified values
 *And also calculates perimeter and area of the created polygons. At the end,
 *all variables of polygons converted to string in order to print out object.*/

class RegularPolygon {
	
	//Define variables of polygon private, so only this class can access them
	private int n = 3;
	private double side = 1;
	private double x = 0;
	private double y = 0;
	
	//Create an object with default values
	public RegularPolygon(){
		
	}
	
	
	//Create an object with side and length values only
	public RegularPolygon(int sideValue1, double lengthValue1){
		
		n = sideValue1;
		side = lengthValue1;
		
	}
	
	
	//Create an object with specified all values of regular polygon
	public RegularPolygon(int sideValue2, double lengthValue2,
							 double xCoordinate, double yCoordinate){
		
		n = sideValue2;
		side = lengthValue2;
		x = xCoordinate;
		y = yCoordinate;
		
	}
	
	
	//Create public method in order to get side value of regular polygon from main class
	public int getSideValue(){
		
		return n;
		
	}
	
	
	//Create public method in order to change side value of regular polygon from main class
	public int setSideValue(int setSide){
		
		n = setSide;
		
		return n;
		
	}
	
	
	//Create public method in order to get length value of regular polygon from main class
	public double getLengthValue(){
	
		return side;
	
	}
	
	
	//Create public method in order to change length value of regular polygon from main class
	public double setLengthValue (double setLength){
		
		side = setLength;
		
		return side;
	}
	
	
	//Create public method in order to get x-coor. value of regular polygon from main class
	public double getXCoordinate(){
		
		return x;
		
	} 
		
	
	//Create public method in order to change x-coor. value of regular polygon from main class
	public double setXCoordinate (double setX){
		
		x = setX;
		
		return x;
		
	}	
	
	
	//Create public method in order to get y-coor. value of regular polygon from main class	
	public double getYCoordinate(){
		
		return y;
		
	}	
		
	
	//Create public method in order to change y-coor. value of regular polygon from main class	
	public double setYCoordinate(double setY){
		
		y = setY;
		
		return y;
		
	}	
		
		
	//Create public method in order to get perimeter value of regular polygon from main class	
	public double getPerimeter(){
		
		return n * side;
		
	}
	
	
	//Create public method in order to get perimeter value of regular polygon from main class	
	public double getArea(){
		
		//Define two variable to calculate area
		double numerator;
		double denominator;
		
		//Formula of the calculating area of the regular polygon used below with specifed values
		numerator = n * side * side;
		denominator = 4 * (Math.sin(Math.PI / n) / Math.cos(Math.PI / n));
		
		//Find area with divising finding values
		double area = numerator / denominator;
		
		return area;
		
	}
	
	
	//Convert properties of regular polygon into string in order to print the object's values
	public String toString(){
		
		String result = "Regular Polygon: \n" +
							"\t" + "Side numbers: " + n + "\n" +
								"\t" + "Length value: " + side + "\n" +
									"\t" + "Coordinate of center: (" +x+ "," +y+ ")\n";
			
		return result;
		
	}
	
}
