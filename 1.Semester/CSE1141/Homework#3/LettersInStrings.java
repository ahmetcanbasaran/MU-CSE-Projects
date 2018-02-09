/*This program find the given letters which 
 *they seperated with '*' character even any 
 *other character that different from 
 *uppercase and lowercase letters*/

import java.util.Scanner;

class LetterInStrings {
	
	//Scans the patterns and strings
	public static String Scan(int number){
		
		Scanner input = new Scanner(System.in);
		
		//Scan pattern only one time
		if(number == 1){
		
			System.out.println("Enter the pattern string: ");
		
			String input1 = input.nextLine();	//Get the whole line
			
			return input1;
		
		//Scan string many times until the user want to exit
		} else {
			
			System.out.println("Enter a string: ");
		
			String input2 = input.nextLine();	//Get the whole line						
			
			return input2;
			
		}
		
	}
	
	
	//Shows the result
	public static void print (String pLetter , String pSentence){
		
		System.out.printf("%s occurs in \"%s\" \n\n", pLetter, pSentence);
		
	}	
	
	//Control the main situation and get true or false
	public static boolean occursIn(String pattern, String str){
		
		int a = 0;		//It is in order to search after the previous match of letter
		int b = -1;		//It is in order to find if the previous pattern is letter
		
		String matches = "";		//Define the matches at he begining empty
		
		//Start to take characters until begining to end
		for (int i = 0; i < pattern.length(); i++){
		
			//Find character
			char patLet = pattern.charAt(i);

		
			//Calculate character value
			int intPatLet = (int)patLet;
					
		
			//Control wheter the pattersn is letter
			if ( 65 <= intPatLet && intPatLet <= 90 
				|| 97 <= intPatLet && intPatLet <= 122 ){
				
				
				//Avoid the error that occurs when control character at -1 order
				if (i != 0){
					
				
					//Find previous character
					char preChar = pattern.charAt(i-1);

					
					//Calculate value of the previous character
					int intPreChar = (int)preChar;

				
					//Control the previous character is letter or not
					//If it is letter, it must be occur after, side by
					//side the previous character
					if (65 <= intPreChar && intPreChar <= 90 
						|| 97 <= intPreChar && intPreChar <= 122 ){
	

						//Find string character
						char strChar1 = str.charAt(a);
						

							//Increase value of a in order to start to search 
							//after previous matches for next pattern
							a++;
			
						
						//If they matches, write the result in string
						if ( patLet == strChar1){												
						
							matches += patLet;

							//Assing to a into b to avoid checking
							//second time in for loop below
							b = a;
						
						}
					
					}
					
				}
								
				
				//Works if the previous pattern of the 
				//this time pattern is not letter
				if ( a != b){						
			
					//Start to search characters from the before place
					for (int j = a; j < str.length(); j++){			
				
						//Find character
						char strChar2 = str.charAt(j);			
				
						
						if (strChar2 == patLet){					
					
							matches += patLet;						
					
							a++;					
					
							break;
					
						}
				
					}
				
				}
			
			}
			
			else{
			
				
				a++;			
		
			}
		
		}
		
		//Throw away '*' character in pattern
		String changedPattern = pattern.replaceAll("[*]" , "");	
		
		//Check wheter the new pattern equals to matches
		boolean controller = changedPattern.equals(matches);	
		
		if (controller)
			
			return true;
			
		else
			
			return false;		
		
		
	}

	
	public static void main (String[] args){
		
		String letters = Scan(1);	//Scan pattern only one time
		
		boolean desire = true;		//Find the user want to continue or stop
		
		//If user want to continue to searching
		while (desire){
		
			//Scan the new sentence
			String sentence = Scan(2);
		
			//If new sentence equals to "exit", so the user want to exit and change desire
			if (sentence.equals("exit")){
			
				desire = false;
			
				System.out.println("Bye");
			
				break;
			
			}
		
		//Controls the patterns to occurs in string
		boolean controller = occursIn(letters, sentence);	
		
		//Display the result wheter it occurs or not
		if (controller)
			print(letters, sentence);
		
		else 
			System.out.printf("%s does NOT occur in \"%s\" \n" , letters, sentence);
	} 
	
}
}