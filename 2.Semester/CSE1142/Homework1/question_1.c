//Oguzhan BÖLÜKBAS, 150114022, HW1Q1.

/*This program get at the beginning spedd, angle and time step values from the user. Then, it calculates 
total flying time, highest point and the traveled distance on the x axis at the highest point and shows
x and h values with specified time intervals*/

#include <stdio.h>
#include <math.h>

#define PI 3.1415926535
#define G 9.80665

int main (){

	//Define all variables
	float v0, theta, step;
	float vX = 0;
	float vY = 0;
	float h = 0;
	float time = 0;
	float flyingTime = 0;
	float x = 0;
	float highestPoint = 0;
	float highestPointDistance = 0;
	float radianTheta = 0;
	int error = 0;
	float i = 0; 						// counter
	float j = 0; 						//counter
	
	
	//Get the values from the user
	printf ("Enter the V0 value: ");
	scanf("%f" , &v0);
	
	if(v0 < 0){
	
		printf("Instantaneous speed have to be greater than zero in projectile motion!");
	
		error = 1;
		
		return -1;
	
	}
	
	printf ("Enter the theta value: ");
	scanf("%f" , &theta);
	
	if (theta < 0 || theta > 90){
	
		printf("The angle have to be between 0 and 90 degree!");
	
		error = 1;
		
		return -1;
		
	}
	
	printf ("Enter the time step value: ");
	scanf("%f" , &step);
	
	if (step < 0){
	
		printf("The time intervals have to be positive!");	
	
		error = 1;
		
		return -1;
		
	}
	
	if (error != 1){
	
		//Calculate the equivalent radian value of obtained degree
		radianTheta = theta * PI / 180;
		
		//Calculate speeds of x and y axises
		vX = v0 * cos(radianTheta);
		
		vY = v0 * sin(radianTheta);
		
		//Calculate the time of reaching to the top point
		time = vY / G;
		
		//Generate flying time
		flyingTime = time * 2;
		
		if(step > flyingTime){
		
			printf("The time intervals is greater than flying time");
			
			return -1;
		
		}
		
		//Display the speeds
		printf ("\nVy is: %.4f \n\n" , vY);
		printf ("Vx is: %.4f \n\n" , vX);
		
		//Display total flying time
		printf("Total flying time is: %.6f \n\n" , flyingTime);
		
		//Start the showing of heights
		printf("h = \n \t");
		
		do {
		
			//Calculate the heights with obtained, generated and constant values
			h = (vY * i) - (G * i * i / 2);
			
			//Find the highest point
			if( h > highestPoint){
			
				highestPoint = h;
				
				highestPointDistance = vX * i;
							
			}
			
			//Show the values
			printf("%.5f \t" , h);
		
			//Increase the counter with wime interval(step)
			i += step;
		
		} while ( i < flyingTime);
		
		
		//Start to display traveled distance on the x-axis
		printf("\n \nx = \n \t");
		
		
		do {
		
			//Calculate traveled distance
			x = vX * j;
		
			printf("%.5f \t" , x);
		
		
			//Increase the counter
			j += step;
		
		} while ( j < flyingTime);
		
		
		//Show the other important things
		printf("\n\nHighest point is: %.4f" , highestPoint);
		
		printf("\n\nDistance at highest point is: %.4f" , highestPointDistance);
		
		printf("\n\nBye...");
		
		return 0;
		
	} else {
	
	
		return -1;
		
	}

}
