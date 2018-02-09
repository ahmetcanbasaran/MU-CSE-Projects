//Oguzhan BÖLÜKBAS, 150114022, HW1Q1.

/*This program gets six numbers from the user. The numbers are between 1 and 49 and also not repeat. If they
are not, the decleared warning(s) will be printed. After obtaining correct input, the program generates five
rows and each row contains six randomly generated numbers which obey above rules and show number of matches  */


#include <stdio.h>

#define MAX 49	//Max value for numbers
#define MIN 1	//Min value for numbers


int main(){

	//To obtain different numbers, time have to be decleared null
	srand(time(NULL));
	
	int number[6]; 				//6 input
	int gNumber[6];				//6 generated numbers
	int matches = 0;			//Matches for generated and obtained numbers
	int i, j, k, l, m, n, o;	//Counters for each for loop
	int correctInput = 1;		//To check whether the input is correct
	int maxValue = 49;			//To check whether the input is correct
	int minValue = 1;			//To check whether the input is correct
	int repetition = 0;			//To check whether the input is correct
	
	
	//Get the input from user
	printf("Enter your lottery numbers: ");
	scanf("%d %d %d %d %d %d" , &number[0], &number[1], &number[2], &number[3], &number[4], &number[5]);
	
	
	//Check whether the inputs are between 1 and 49
	for( m = 0; m < 5; m++){
	
		if(number[m] > maxValue)
		
			maxValue = number[m];
			
		if(number[m] < minValue)
		
			minValue = number[m];
	
	}
	
	if (maxValue > 49 || minValue < 1){
	
		printf("The numbers have to be between 1 and 49! \n");
		
		correctInput = 0;
	
	}
	
	
	//Check whether the inputs are repeated numbers
	for (n = 0; n < 6; n++){
					
		for(o = 0; o < 6; o++){
		
			if(number[n] == number[o] && n != o){
				
				repetition = 1;
							
			}
		
		}
		
	}
	
	if(repetition == 1){
	
		printf("The numbers have not to repeat! \n");
	
	}
	
	
	//If everthing is correct, the main function will start
	if(correctInput != 0 && repetition != 1){
	
	
		//This for loop is generated for 5 rows of output
		for( k = 0; k < 5; k++){
		
			matches = 0;
		
		
			//This for loop decleares random numbers
			for (i = 0; i < 6; i++){
				
				
				//Declearing random numbers between 1 and 49
				gNumber[i] = (MIN + (rand() % MAX));
				
				
				//Check whether the randomly generated numbers repeat
				for(l = 0; l < i; l++){
				
					if(gNumber[i] == gNumber[l]){
					
						gNumber[i] = (MIN + (rand() % MAX));
						
					}
				
				}
				
				
				//Check whether the randomly generated numbers repeat one more time
				for(l = 0; l < i; l++){
				
					if(gNumber[i] == gNumber[l]){
									
						gNumber[i] = (MIN + (rand() % MAX));
						
					}
				
				}
				
				
				//Check whether the randomly generated numbers repeat again in order to avoid repeatitions
				for(l = 0; l < i; l++){
				
					if(gNumber[i] == gNumber[l]){
									
						gNumber[i] = (1 + (rand() % 49));
						
					}
				
				}
				
				
				//If the randomly generated numbers equals to obtained numbers, increase the match number
				for (j = 0; j < 6; j++){
				
					if(gNumber[i] == number[j]){
					
						matches++;
						
					}
				
				}	
				
			}
			
			
			//Display the randomly generated numbers and the value of match(es)
			printf("\n\n%d \t %d \t %d \t %d \t %d \t %d \t %d" , gNumber[0], gNumber[1], gNumber[2], gNumber[3], gNumber[4], gNumber[5], matches);
		
		}	//End of main for loop
		
	}	//End of if
	
	return 0;	

}	//End of main function
