//This program calculates least cmmon multiple of two integers

import java.util.Scanner;	//Import Scanner to obtain the integers from user

class LeastCommonMultiple {
	
	public static int Scan(){
		
		Scanner input = new Scanner(System.in);		//Define the input method
		
		System.out.print("Please enter an integers: ");	//Show message to user
		
		int number = input.nextInt();	//Get input like integer
		
		return number;
		
	}
	
	public static void main (String[] args){
		
		int lcm = 2;					//Define least common user and assing the least prime number(2)
		boolean controller = true;		//Define an controller in order to avoid to run program with values those are less than zero
		int max = 0, min = 0;			//Define maximum and minimum number to calculate easily (It has explained below)
		
		int number1 = Scan();	//Get input1
		int number2 = Scan();	//Get input2
		
		//Find the maximum and minimum value between obtained integers
		if ( number1 > number2 ){
			
			max = number1;
			min = number2;
			
		} else {
			
			max = number2;
			min = number1;
		
		}
		
		
		
		
	
		//Avoid to run program with values that are negative or zero
		if (number1 <= 0 || number2 <= 0){
						
			System.out.println("The integers must be greater than zero!");
			controller = false;
			
		}	
			
			
		
		
		
		while ( controller ){
			
			//First control that is the maximum value multiple of 
			//minimum value in order to avoid more turns of loops
			if (max % min == 0){
				
				System.out.println("Least common multiple of the integers is: " + max);
				break;	//If this is true, exit the loop because we use least common multiple easily
			
			//Program controls the number can divide the lcm without any remainder	
			} else if (lcm % number1 == 0 && lcm % number2 == 0) {
				
				System.out.println("Least common multiple of the integers is: " + lcm);
				break;	//If this is true, exit the loop because we find it			
				
			} else {
				
				lcm++;	//Increase least common multiple until find the correct one
				
			}	//End of else
			
		}	//End of while
	
	}	//End of main 
	
}	//End of class
				
		
	