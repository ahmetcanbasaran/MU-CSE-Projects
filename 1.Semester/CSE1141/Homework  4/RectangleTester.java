/*This program have two part. One of them is Rectangle class that creates
 *rectangle object with argument and without argument. The another class is
 *main class. In that, width and height variables assigned. Then, the object
 *displayed on the screen with informations and area and perimeter values*/

class RectangleTester {
	
	public static void main (String[] args){
		
		//Specify object in Rectangle class
		Rectangle r1, r2;
		
		//Create a new object with it's values
		r1 = new Rectangle(4 , 40);
		r2 = new Rectangle(3.5 , 35.9);
		

		//Print the first object and its perimeter and area values
		System.out.printf("Rectangle 1: \n%s" , r1);
		System.out.printf("\n\tRectangle's area: %.2f" , r1.getArea());
		System.out.printf("\n\tRectangle's perimeter: %.2f \n\n" , r1.getPerimeter());
		
		//Print the second object and its perimeter and area values
		System.out.printf("Rectangle 2: \n%s" , r2);
		System.out.printf("\n\tRectangle's area: %.2f" , r2.getArea());
		System.out.printf("\n\tRectangle's perimeter: %.2f \n" , r2.getPerimeter());
		
	}
}
