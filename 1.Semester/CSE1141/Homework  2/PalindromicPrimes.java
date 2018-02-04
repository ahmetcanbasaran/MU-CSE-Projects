/*This program shows the first 100 prime and also palindromic numbers*/

class ad {

	//This method controls that is the number prime or not	
	public static boolean primeController (int number1){
		
		int primeNumber = number1;	//Take the came number
		boolean result1 = true;		//Create a result and return true
		
		//This loop turns until find the number is prime or not		
		for(int divisor = 2; divisor <= primeNumber /2 ; divisor++ ){
			
			//If divisor can divede the number without nay remainder different from 0 returns false
			if(primeNumber % divisor == 0){
				result1 = false;
				break;	//Exit the for loop
			}			
		}
		
		return result1;
		
	}
	
	//This method controls that is the number palindrom or not		
	public static boolean palindromController (int number2){	
		
		boolean result2 = false;
		int number3 = number2;
		int originalNumber = number2;
		int reverseNumber = 0;
		
		//This loop supports the reverse number to compare to the original number
		while (number3 > 0){
			
			int lastDigit = number3 %10;
			reverseNumber = (reverseNumber * 10) + lastDigit;
			number3 /= 10;
			
		}
		
		//If the original number and the reverse number same this assing result2 true
		if (originalNumber == reverseNumber)
			result2 = true;
		
		return result2;
		
	}
	
	public static void main (String[] args){
		
		final int WRITE_NUMBER = 100;	//We want see the only 100 palindromic primes 
		int writtenNumber = 0;
		int number = 2;
		
		//This loop turns until reach the first 100 palindromic primes
		while (writtenNumber < WRITE_NUMBER){
				
				//This statement controls the number with methods help
				if (primeController(number) && palindromController(number)){
					
					System.out.print(number + " ");
					writtenNumber++;
					
					//When the program write 10 palindromic primes, it passes under line
					if (writtenNumber % 10 == 0)
						System.out.println();
			
				}	//End of if
				
				number++;
				
		}	//End of while 
			
	}	//End of main method
		
}	//End of class
