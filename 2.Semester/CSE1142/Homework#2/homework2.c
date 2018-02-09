/*	CSE142 - Spring 2016 
	Homework #2

	Due: May10th,2016, 23:55	*/

/* Oguzhan BÖLÜKBAS, 150114022, HW2 */

/*This program repeatedly reads an expression from the user that is made up of 
digits, +, - and parentheses, and evaluates the expression in modulo 10 and prints 
the result; if the expression is malformed the program will give an error message*/

#include <stdio.h>

//functions' prototypes
int select (char[]);
int calculate (char[]);

//declare counter and boolean
int c;
int isCorrect = 1;
 
int main(){

	//Generate an array with size 50. I think, this is enough. You can increase it, if you wish
	char input[50];
	
	//For finding priority, these variables are decleared
	int leftBrNum = 0;
	int rightBrNum = 0;
	
	//Declare variable in order to check correct input
	int correctNum = 0;
	int correctChar = 0;
	int correctBrNum = 0;

	//Assign all char to NULL
	for(c = 0; c < 50 ; c++){
	
		input[c] ='\0';
		
	}

	//The main input loop. It ends with '*'
	do {
	
		isCorrect = 1;
		correctBrNum = 0;
		correctNum = 0;
		correctChar = 0;
		
		leftBrNum = 0;
		rightBrNum  = 0;
		
		for(c = 0; c < 50 ; c++){
	
			input[c] ='\0';
		
		}
	
		printf("Enter expression: ");
		
		scanf("%s" , input);
		
		if(input[0] == '*'){
		
			printf("Bye!");
		
			return 0;
		
		}
		
		//Input controlling
		for(c = 0; c < 50 ; c++){
		
			if(input[c] != '\0'){
			
				correctNum = 0;
				correctChar = 0;
				correctBrNum = 0;
			
			
				//Count the braces numbers for '(' and ')'
				if(input[c] ==  '('){
				
					leftBrNum++;
					
				}
					
				if(input[c] ==  ')'){
				
					rightBrNum++;
					
				}
					
				if(rightBrNum == leftBrNum)
				
					correctBrNum = 1;	
				
				if(input[c] >= '0' && input[c] <= '9' ){
				
					correctNum = 1;
				
				}
					
				if(input[c] == '(' || input[c] == ')' || input[c] == '+' || input[c] == '-'){
				
					correctChar = 1;
					
				}
					
				if(correctNum == 0 && correctChar == 0)
				
					break;
				
			}
		
		}
		
		
		//If the input is wrong, finish the processing it
		if(correctChar == 0 && correctNum == 0){
		
			printf("ERROR\n\n");
		
		} else if (correctBrNum == 0){
		
			printf("ERROR\n\n");
		
		//Start to process when the input is correct
		} else {		
						
			int result = select(input);
			
			//Modulo 10			
			while ( result > 10){
			
				result -= 10;
			
			}
			
			if(isCorrect == 0){
			
				printf("ERROR\n\n");
			
			} else {
			
				//Modulo 10
				if(result < 0)
			
					result += 10;
			
				printf("%d\n\n" , result);
		
			}
		
		}
	
	} while(input[0] != '*');	
	
}	//End of main


//This function selects numbers in the most inner paranthesis 
//and send them to calculate function
int select (char exp[]){

	int leftmostBr = 0;
	int rightBr = 0;
	
	int finish = 0;
	int noBr = 0;
	
	int preResult = 0;
	
	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	
	//New char array for this function
	char miniExp[50];
	
	//Assign to null 
	for(a = 0; a < 50; a++){
	
		miniExp[a] = '\0';
	
	}
	
	//It returns until the braces will finish
	while (noBr == 0){
		
		leftmostBr = 0;
		rightBr = 0;
		
		for (a = 0; a < 50; a++){
	
			if(exp[a] == '('){
			
				leftmostBr = a;
					
			}
			
			if(exp[a] == ')'){
			
				rightBr = a;
								
				break;
			
			}
			
		}
		
		if(leftmostBr == 0 && rightBr == 0){
		
			noBr = 1;
			
			break;
		
		}
		
		//'Cut' the numbers which will be processing from the input		
		for	(b = leftmostBr; b < (rightBr - 1) ; b++){
					
			miniExp[b - leftmostBr] = exp[b + 1];
			
		}
		
		//To avoid this wrong input: '()'
		if(leftmostBr + 1 == rightBr){
		
			isCorrect = 0;
			
			return 0;
		
		}
		
		//Take the result of sent numbers				
		preResult = calculate(miniExp);
		
		//Replace the obtained result with sent numbers in array				
		for(d = 0; d < 50; d++){
		
			if(d < leftmostBr){
		
				exp[d] = exp[d];
											
			} else if (leftmostBr <= d && d <= rightBr){
			
				exp[leftmostBr] = '0' + preResult;
											
			} else {
			
				exp[d - (rightBr - leftmostBr)] = exp[d];
								
			}			
		
		}
			
	}
	
	//Take the last result when the inputs have any brace
	int result = calculate(exp);
	
	return result;

}

int calculate (char operand[]){ 

	int lastNum = 0;
	int preResult = 0;
	int e;
	
	int hasOperator = 0;
	
	//It works in order to find the input is '4+5' for example or '9' , '-9' , -(9)' and so on.
	if(operand[1] == '+' || operand[1] == '-')
	
		hasOperator = 1;
	
	
	//If the obtained input is only a number without any operator, this works
	if (operand[0] >= '0' && operand[0] <= '9' && hasOperator == 0){
	
		return operand[0] - '0';
		
		
	//Returns the correct value if obtained number is '-9' or '+7' for example
	} else if (operand[0] == '+' || operand[0] == '-'){
	
		switch(operand[0]){
		 
			case('+'):
				
				return operand[1] - '0';
				
				break;
			
			
			case('-'):
			
				return 10 - (operand[1] - '0');
			
				break;
			
		}
	
	//If the input have one or more operator, it works until getting a one digit result
	} else {
	
		for(e = 0; e < 50; e++){
	
		if ( e % 2 == 1){
		
			switch(operand[e]){
			
				//Rearrange the input array with founded results and the calculated numbers			
				case('+'):
				
					preResult = (operand[e - 1] - '0' ) + (operand[ e + 1] - '0');
					
					operand[e + 1] = preResult + '0';
					
					break;
					
				
				case('-'):
				
					preResult = (operand[e - 1] - '0' ) - (operand[ e + 1] - '0');
					
					operand[e + 1] = preResult + '0';
					
					break;
			
			}
		
		}
	
	} 
		
		return preResult % 10;
		
	}
	
}
