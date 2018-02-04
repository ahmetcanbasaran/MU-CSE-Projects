/*This program has two class which one is main and the other is RegularPolygon
 *Main class creates three different type polygon with using RegularPoygon class
 *First one of them has no argument, the second has only side and length value
 *and third has side, length and also coordinates numbers. At the end of the program
 *it will display the three object's area and perimeter values*/

class RegularPolygonTester {
	
	public static void main(String[] args){
	
	//Define variables that associated with RegularPolygon class	
	RegularPolygon r1, r2, r3;
	
	//Create object with specifying some variables of them
	r1 = new RegularPolygon();
	r2 = new RegularPolygon(6, 4);
	r3 = new RegularPolygon(10, 4, 5.6, 7.8);
	
	//Display the object's area and perimeter values on the screen
	System.out.printf("Regular Polygon 1: \n\tPerimeter: %.3f\n\tArea: %.3f\n\n" ,
						r1.getPerimeter() , r1.getArea());
	System.out.printf("Regular Polygon 2: \n\tPerimeter: %.3f\n\tArea: %.3f\n\n" ,
						r2.getPerimeter() , r2.getArea());
	System.out.printf("Regular Polygon 3: \n\tPerimeter: %.3f\n\tArea: %.3f\n\n" ,
						r3.getPerimeter() , r3.getArea());	
		
	}
}
