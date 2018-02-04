/*This program compare two rectangle which are specify by the user
 *wheter second is inside one or second overlap one or not overlap and inside */



//Import Scanner class in order to obtain data from user
import java.util.Scanner;


class TwoRectangles {
	
	
	public static void main(String [] args) {
		
		
		Scanner sc = new Scanner (System.in);   //Identify a scanner function like sc
		
		
		//Represent to user to input values which are programs wants
		System.out.print("Enter r1's center x- , y-coordinates, width and height: "); 
			
		
		//Seperate the taken strings into correct parts and convert them to double value	
		String sX1 = sc.next();   Double x1 = Double.parseDouble(sX1);
		String sY1 = sc.next();   Double y1 = Double.parseDouble(sY1);
		String sW1 = sc.next();   Double w1 = Double.parseDouble(sW1);
		String sH1 = sc.next();   Double h1 = Double.parseDouble(sH1); 
			
			
		//Repeat above code for second rectangle
		System.out.print("Enter r1's center x- , y-coordinates, width and height: "); 
			
			
		String sX2 = sc.next();   Double x2 = Double.parseDouble(sX2);
		String sY2 = sc.next();   Double y2 = Double.parseDouble(sY2);
		String sW2 = sc.next();   Double w2 = Double.parseDouble(sW2);
		String sH2 = sc.next();   Double h2 = Double.parseDouble(sH2); 
			
			
			
		Double leastPointX1 = x1 - w1;    //Find the least endpoint x of r1
		Double highestPointX1 = x1 + w1;    //Find the highest endpoint x of r1
		Double leastPointY1 = y1 - h1;    //Find the least endpoint y of r1
		Double highestPointY1 = y1 + h1;    //Find the highest endpoint y of r1
		
		
		Double leastPointX2 = x2 - w2;    //Find the least endpoint x of r2
		Double highestPointX2 = x2 + w2;    //Find the highest endpoint x of r2
		Double leastPointY2 = y2 - h2;    //Find the least endpoint y of r2
		Double highestPointY2 = y2 + h2;    //Find the highest endpoint y of r2
		
		
		
		//Write boolean express to control whether r2 is inside to r1 
		if (highestPointX2 < highestPointX1 && leastPointX1 < leastPointX2 && 
			 highestPointY2 < highestPointY1 && leastPointY1 < leastPointY2) {
			 	
			
			 	System.out.println ("r2 is inside r1");
			 	
			 				 	
		//If not inside so control whether its overlaps	
		} else if (leastPointX1 < leastPointX2 && highestPointX1 > leastPointX2 ||
					leastPointX1 < highestPointX2 && highestPointX1 > highestPointX2 ||
					 leastPointY1 < leastPointY2 && highestPointY1 > leastPointY2 ||
					  leastPointY1 < highestPointY2 && highestPointY1 > highestPointY2) {
					  	
			
			 	System.out.println ("r2 overlaps r1");
			 	
			
		//If both inside or overlaps are false, so the program writes that it does not overlap
		} else {
		
		
			 	System.out.println ("r2 does not overlap r1");
			 	
			 	
		}	 	//End of the else
	
	}		//End of the main function
		
}		//End of the class
		