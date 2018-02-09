/*		CSE225/CSE 2025	Data Structures, 2016-2017(FALL) - PROJECT #1 (Due to: 25.10.2016, 18:00)
*
*		Oguzhan BOLUKBAS, 150114022, CENG Student 
*
*		This program can be used in order to multiply huge two numbers 
*	thats their sizes are arbitrary with helps of 3 linked lists. It also
*	saves all the results in external text file which has name "History"
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

//Value is used for digit value and order is used for power of 10, it helps to specify place of numbers
typedef struct digit{

	short value;
	short order;
	struct digit *nextPtr;

}DIGIT;

//The digit pointers defined as global variables in order to use at any time in any functions which we want
DIGIT *linkedList1 = NULL;
DIGIT *linkedList2 = NULL;
DIGIT *resultList = NULL;

FILE *fptr;

//This declerations are used in order to save the time in history
time_t rawtime;
struct tm *timeinfo;

//These global variables are used to specify order of inputs
static short inputNumber1 = 0;
static short inputNumber2 = 0;
static short highestOrder = 0;

//This variables help to define where the point is in input numbers
short point = 0;
short point1 = 0;
short point2 = 0;

//This variables are used to check whether the number(s) is/are negative
short minus = 0;
short minus1 = 0;
short minus2 = 0;

//To find the size of input numbers
short inputSize1 = 0;
short inputSize2 = 0;

//Functions' prototypes
void insert(short, char);
void print(DIGIT*);
void calculate();
void add(short, short);

//Insert the obtained number to target linked list
//Char "a" helps to understand which linked list will be written
void insert(short data, char a){
	
	DIGIT *np = malloc(sizeof(DIGIT));
	
	np -> value = data;
    
    //If a is 1, use linkedList1 pointer
	if(a == '1'){

		np -> nextPtr = linkedList1;
	
		linkedList1 = np;

		linkedList1 -> order = inputNumber1;
	
		inputNumber1++;
	
	//If a is 2, use linkedList2 pointer
	} else if(a == '2'){

		np -> nextPtr = linkedList2;
	
		linkedList2 = np;

		linkedList2 -> order = inputNumber2;

		inputNumber2++;
		
	//If a is not 1 nor 2, use resultList pointer
	} else {
		
		np -> nextPtr = resultList;
	
		resultList = np;
		
	}

}

//This function multplies the linked list values one by one and also defines their orders
void calculate(){
	
	DIGIT *cp1;
	DIGIT *cp2;
	
	//These helps us result of multiplication will be added or inserted
	short newOrder = 0;
	short lowestOrder = 0;
	
	cp1 = linkedList1;
	cp2 = linkedList2;
	
	//The largest numbers are the first nodes of pointers
	highestOrder = (cp1 -> order) + (cp2 -> order);
	
	//This variable helps adding result when orders are equal
	lowestOrder = (cp1 -> order) + (cp2 -> order) + 1;

	while(cp1 != NULL){
				
		cp2 = linkedList2;
			
		while(cp2 != NULL){

			newOrder = (cp1 -> order) + (cp2 -> order);

			//add the result with the same order numbers
			if(newOrder >= lowestOrder) {
				
				add((cp1 -> value) * (cp2 -> value), newOrder);

			//Insert the new order number
			} else {
								
				insert((cp1 -> value) * (cp2 -> value), '0');
			
				resultList -> order = newOrder;

				lowestOrder = newOrder;
			
			}				
			
			cp2 = cp2 -> nextPtr;
				
		}
		
		cp1 = cp1 -> nextPtr;
		
	}
		
}

//To add numbers whichs are have the same order
void add(short data, short order){
		
	DIGIT* aP = resultList;
	
	while(aP -> order != order){
		
		aP = aP -> nextPtr;
				
	}
	
	(aP -> value) = (aP -> value) + data;
		
}

//To define carry out numbers and to add them to the one number higher ordered number
void transfer(){
	
	DIGIT *tP = resultList;
	DIGIT *prePtr = resultList;
	
	short lastDigit;
	short transfer;
	
	short order = highestOrder;
		
	//To find carry out number and rearrange the number
	while(order > 0){
	
		tP = resultList;
	
		while((tP -> order) != order){
			
			prePtr = tP;
			
			tP = tP -> nextPtr;
			
		}
	
		lastDigit = (tP -> value) % 10;
	
		transfer = (tP -> value) / 10;
	
		tP -> value = lastDigit;
	
		prePtr -> value += transfer;
	
		--order;
	
	}
	
	//If the head node has bigger value than 10, the number will be rearranged 
	if((resultList -> value) >= 10){
		
		lastDigit = (resultList -> value) % 10;
	
		transfer = (resultList -> value) / 10;

		resultList -> value = lastDigit;
		
		insert(transfer, '0');
		
	}
	
}

//This functions prints the result linked list from the start point (head)
void print(DIGIT* ptr){

	DIGIT *np = ptr;
	
	short c = 0;
	
	while (np != NULL){
		
		printf("%d" , np -> value);
		
		c++;
		
		if(point == c)
			printf(".");
		
		np = np -> nextPtr;
		
		
	}
	
	printf("\n");

}

void saveHistory(){
	
	//These are used for saving the time in History.text
	time ( &rawtime );
	timeinfo = localtime ( &rawtime );
	
	fprintf (fptr , "%s", asctime(timeinfo) );
		
	DIGIT *np = linkedList1;
	
//***For linkedList1*********************************************
	
	//The biggest order of linkedList1
	short constantOrder = linkedList1 -> order;
	short order	= 0;

	np = linkedList1;
	
	//If the only one number is negative, the the result is negative
	if(minus1 == 1)
		fprintf(fptr , "%s" ,"Number1: -");
	
	else
		fprintf(fptr , "%s" ,"Number1: ");

	//To print the resultList from end of the list
	while(order != constantOrder + 1){
	
		while(np -> order != order){
					
			np = np -> nextPtr;
			
		}
		
		//To write to the text
		fprintf(fptr , "%d" , np -> value);
		
		if(point1 != 0)
			point1 = inputSize1 - point1;	
		
		//To put the '.' character when its order comes
		if(point1 == order + 1)
			fprintf(fptr , "%s" , ".");
		
		np = linkedList1;
		
		++order;

	}
	

//***For linkedList2*******************************************
	
	//All of them have the same plan with the linkedList1
	constantOrder = linkedList2 -> order;
	order = 0;	

	np = linkedList2;
	
	if(minus2 == 1)
		fprintf(fptr , "%s" ,"\nNumber2: -");
	
	else
		fprintf(fptr , "%s" ,"\nNumber2: ");
	
	
	while(order != constantOrder + 1){
	
		while(np -> order != order){
					
			np = np -> nextPtr;
			
		}
		
		fprintf(fptr , "%d" , np -> value);
		
		if(point2 != 0)
			point2 = inputSize2 - point2;	
		
		if(point2 == order + 1)
			fprintf(fptr , "%s" , ".");
		
		np = linkedList2;
		
		++order;

	}
	
	
	if((minus1 + minus2) == 1)
		fprintf(fptr , "%s" ,"\nResult:  -");
	
	else
		fprintf(fptr , "%s" ,"\nResult:  ");
	
	
//***For resultList*****************************************	
	
	
	np = resultList;
	
	short resultSize = 0;
	
	while (np != NULL){
		
		resultSize++;
		
		np = np -> nextPtr;
		
	}
		
	np = resultList;
	
	if(point != 0)
		point = resultSize - point;
	
	short c = 0;
	
	while (np != NULL){
		
		fprintf(fptr , "%d" , np -> value);
		
		c++;
		
		if(point == c)
			fprintf(fptr , "%s" , ".");
		
		np = np -> nextPtr;
		
	}

	
	fprintf(fptr , "%s" , "\n\n");
	
}

int main(){
	
	int size;
	short aC = 0;
	
	fptr = fopen("History.txt", "a");
   
	if(fptr == NULL){
      
	  printf("Error!");
	  
      return 1;
      
	}
	
	//Obtain the size of bigger input to define the array as short as possible
	printf("Enter the size of big input: ");
	scanf("%d" , &size);
	
	char input1[size + 5];
	char input2[size + 5];
		
	printf("Enter number1: ");
	scanf ("%s", input1);
	
	printf("Enter number2: ");
	scanf("%s" , input2);
		
		
//***For input1*************************************************************
		
	//Define that whether input1 is negative	
	if(input1[aC] == '-'){
		
		minus1++;
		
		aC++;
		
	}
	
	
	//Start to put the numbers from array to linkedList1
	while(input1[aC] <= '9' && input1[aC] >= '0' || input1[aC] == '.'){
		
		if(input1[aC] == '.'){
						
			if(minus1 == 1)
				point1 = aC -1;
			else
				point1 = aC;
			
			aC++;
			
		} else {
			
			insert(input1[aC] - '0' , '1');
		
			aC++;
			
			inputSize1++;
			
		} 
			
		
	}
			
			
//***For input2*************************************************************
			
			
	aC = 0;
		
	if(input2[aC] == '-'){
		
		minus2++;
		
		aC++;
		
	}
		
	while(input2[aC] <= '9' && input2[aC] >= '0' || input2[aC] == '.'){
		
		if(input2[aC] == '.'){
						
			if(minus2 == 1)
				point2 = aC -1;
			else
				point2 = aC;
			
			aC++;
			
		} else {
									
			insert(input2[aC] - '0' , '2');
		
			aC++;
			
			inputSize2++;
			
		} 
			
		
	}
	
	//To define that where the point must be in the result
	if(point1 != 0)
		point1 = inputSize1 - point1;
		
	if (point2 != 0)
		point2 = inputSize2 - point2;
		
	point = point1 + point2;

	//To call this function to multiply the numbers and add or insert them
	calculate();

	//To calculate carry in and carry out numbers and transfer them to next node(DIGIT)
	transfer();

	//Save the input numbers and the result to the text file
	saveHistory();	

	//To check whether the result must be positive
	if((minus1 + minus2) == 1)
		printf("Result: -"); 
		
	else
		printf("Result: "); 	
	
	print(resultList);
	
	fclose(fptr);
	
	return 0;
	
}
