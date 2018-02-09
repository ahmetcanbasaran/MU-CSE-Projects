/*This program calculates square root of given value
 *using the ancient way to finding square root which
 *is Babylonian methods and show the result at least
 *5 significant figures. */

import java.util.Scanner;		//Import Scanner to get input from user

class SquareRoot {
	
	public static double sqrt(long n){
	
		double lastGuess = (Math.random() * n);		//Generate a number between 0 and number
		double nextGuess = 0;						//Create next guess to get close to result
		
		while (true){
			
			//Calculate next guess with using Babylonian method
			nextGuess = ( lastGuess + n /lastGuess ) / 2;
			
			//Find the difference between last and next guess
			Double difference = Math.abs(lastGuess - nextGuess);
			
			//This program turns until reaches the result less than 0.0001 difference
			if (difference < 0.0001){		
					
				break;			
					
			}			
			
			//Assing the finding new value to old value
			lastGuess = nextGuess;			
			
		}		
		
		return nextGuess;		
		
	}
	
	
	//Takes the word from user and converts it like value type of long and returns it
	public static long scan(){
		
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter a number: ");
	
		long number = input.nextLong();
		
		return number;
		
	}
	
	

	public static void main (String[] args){
		
		long n = scan();	//Get number from user with using scan method
		
		double result = sqrt (n);	//Send number to sqrt method and get it like double value
		
		//Print the result with 4 significant figures after the dot
		System.out.printf ("Square root of the number is aproximately %.4f" , result);
		
	}
	
}
