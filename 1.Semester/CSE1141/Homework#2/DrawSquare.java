/*This program draws a square with the obtained value 
 *from the user to determine the border distance of square*/

import java.util.Scanner;	//Import scanner to get input from user

class DrawSquare {
	
	//This method shows output to user, 
	//get output from user and convert the string(input) into integer
	public static int Scan(){
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter a number: ");
			
		int number = input.nextInt();	//Obtain and convert the string into the number
		
		return number;
		
	}	//End of Scan method
	
	public static void main (String[] args){
		
		int number = Scan();	
		
		//This loop supplies to draw lines under then under (obtained number minus one) times
		for ( int i = 0; i < number; i++){
			
			//This loop supplies to draw a line with charecters obtained number minus one times
			for ( int j = 0; j < number; j++){
				
				//This controlls and draws the borders of the square
				if ( i == 0 || j == 0 || i == number - 	1 || j == number - 1)
					System.out.print("*");
				
				//When the number of characters reach the end of the line, it passes under line	
				if( j == number-1)
					System.out.println();
				
				//Put multiple sembol like desired	
				if ( (i + j) % 2 == 0 && i != 0 && j != 0 && i != number-1 && j != number-1)
					System.out.print("+");
				
				//Put multiple sembol like desired
				if ((i + j) % 2 != 0 && i != 0 && j != 0 && i != number-1 && j != number-1)
					System.out.print(" ");
				
			} // End of inside for loop
			
		}	//End of outside for loop
		
	}	//End of main method
	
}	//End of class
	

