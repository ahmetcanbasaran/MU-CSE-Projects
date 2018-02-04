/*This program find the suffix of the two given words.
 *Firstly it takes 2 word, then reverses they and compares
 *the reversing words' characters from the begining until 
 *they are not equal. Then reverses the finding suffix in 
 *order to show the user correctly like written order  */


import java.util.Scanner;	//Import to get input (words) from user

class CommonSuffix {

	/*This methods defines input to scan, gets word, 
	* takes the word in string object and returns it*/
	public static String scan(){
		
		Scanner input = new Scanner (System.in);
		
		System.out.println("Enter a word: ");
		
		String word = input.next();
		
		return word;
		
	}
	
	//Reverse the sending string
	public static String reversing (String reversable){		
		
		//Define reversed string as empty
		String reversed = "";
		
		//Find the length of taken string
		int length = reversable.length() - 1;
		
		/*Reverse taken string w,th for loop 
		* which supplies writing first letter at the end */
		for (int i = length; i >= 0; i--){
			
			reversed += reversable.charAt(i);
			
		}				
		
		return reversed;
		
	}
	
	/*Find which word is shorter for the stoping value of for loop and
	 *compare all characters from begin to end until finding not equal situation*/
	public static String commonSuffix (String s1, String s2){
		
		String rResult = "";
		
		int lenWord1 = s1.length();		//Length of first word
		int lenWord2 = s2.length();		//Length of second word
		int wLength = 0;				//Length of shorter worder, at the begining 0
		
		
		if (lenWord1 > lenWord2)	//Compare and find shorter word's length
			wLength = lenWord2;
		else
			wLength = lenWord1;	
			
			
		
		for (int j = 0; j < wLength; j++){
		
			char c1 = s1.charAt(j);		//Find the j'th character from begining at word1
			char c2 = s2.charAt(j);		//Find the j'th character from begining at word2
			
			if (c1 != c2)				//Stop when the not equal
				break;
				
			else
				rResult += c1;			//Store characters in string when they equal
		
		}
		
		return rResult;
		
	}
	
	//This method displays the result to user on the screen
	public static void print (String result){
		
		System.out.printf ("Common suffix of the given words is: -%s" , result);
		
	}

	public static void main (String[] args){
		
		String word1 = scan();		//Take first word with using scan method
		String word2 = scan();		//Take second word with using scan method
		
		String rWord1 = reversing(word1);		//Reverse it with using reverse method
		String rWord2 = reversing(word2);		//Reverse it with using reverse method
		
		String rSuffix = commonSuffix(rWord1, rWord2);		//Take reversable suffix
		
		String suffix = reversing(rSuffix);		//Reverse the finding suffix
		
		print(suffix);		//Print the result
		
	}

}
