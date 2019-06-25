#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

/* ---- Job transaction ---- */ 
/* ---- [customer_id] - [operation_id] - [product_id] - [number_of_product] ---- */

// mutex for each seller
pthread_mutex_t *seller_mutex;

// mutex for each product
pthread_mutex_t *product_mutex;

int number_of_customers, number_of_sellers,number_of_simulation_day,number_of_products;

// number of each product beginning of a day
int *products;

// number of each avaliable products
int *available_products;

// info of each customer's rezervation limit and product limit
int **customer_informations;

// info transaction from customer to seller
int **job_transaction;

// job for seller
int *seller_work;

//customer threads
void *customer(void *threadid){
	long thread_id = (long) threadid;
	
	//int random_operation = rand() % 3;
	int random_operation = 0;	
	int random_product = rand() % number_of_products;
	int random_product_number = rand() % products[random_product];
	
	int locked = -1;
	int seller_id;
	int i = 0;
	while( locked != 0 ){
		locked = pthread_mutex_trylock(&seller_mutex[i]);
		if( locked == 0 ){
			seller_id = i;
		}
		else if ( i + 1 == number_of_sellers ){
			i = 0;
		}
		else{
			i++;
		}
	}
	
	// buy operation
	if( random_operation == 0){
		job_transaction[seller_id][0] = thread_id;
		job_transaction[seller_id][1] = 0;
		job_transaction[seller_id][2] = random_product;
		job_transaction[seller_id][3] = random_product_number;

		seller_work[seller_id] = 1;
	}

	// reserve operation
	else if( random_operation == 1){
		
	}

	// cancel reserve operation
	else{
	}	
}



//seller threads
void *seller(void *threadid){
	long thread_id = (long) threadid;
	
	int customer_operation;
	int customer_id;	
	int product_id;
	int product_number;

	while( seller_work[thread_id] == 0 ); // wait for a work
	
	customer_id = job_transaction[thread_id][0];
	customer_operation = job_transaction[thread_id][1];
		
	// customer's buy operation
	if( customer_operation == 0 ){
		product_id = job_transaction[thread_id][2];
		product_number = job_transaction[thread_id][3];
		
		pthread_mutex_lock(&product_mutex[product_id]);
		//printf("%d	%d	%d	%d\n",product_id,customer_id,available_products[product_id], product_number);
		if ( available_products[product_id] < product_number ){
			pthread_mutex_unlock(&product_mutex[product_id]);
			printf("%d - There is no avaliable source\n",customer_id);		
		}
		else{
			available_products[product_id] = available_products[product_id] - product_number;
			pthread_mutex_unlock(&product_mutex[product_id]);
			printf("Customer#%d Buy_operation 1\n", customer_id);
		}
	}
	// customer's reserve operation
	else if ( customer_operation == 1 ){
		
	}
	// customer's cancel operation
	else if ( customer_operation == 2 ){
	}
	else{
		printf("Undefined operation\n");
	}
	
	pthread_mutex_unlock(&seller_mutex[thread_id]);

}


void customer_var_initialization(){
	int i = 0;

	// create [number_of_customers][2] global_matrix   
       	customer_informations = calloc( number_of_customers, sizeof (int *));
       	for (i = 0; i < number_of_customers; i++)
      	 	customer_informations[i] = (int *) calloc( 2, sizeof (int));

}

void seller_var_initialization(){
	int i = 0;

	seller_work	 = calloc( number_of_sellers, sizeof (int));
	
	seller_mutex = malloc( sizeof(pthread_mutex_t) * number_of_sellers);
	for(i = 0; i < number_of_sellers; i++)
		pthread_mutex_init(&seller_mutex[i], 0);	


	job_transaction = calloc( number_of_sellers, sizeof (int *));
       	for (i = 0; i < number_of_sellers; i++)
      	 	job_transaction[i] = (int *) calloc( 4, sizeof (int));

}


void product_var_initialization(){
	int i;

	// allocate memory for products
	products = calloc( number_of_products, sizeof (int));
	available_products = calloc( number_of_products, sizeof (int));
	
	product_mutex = malloc( sizeof(pthread_mutex_t) * number_of_products);
	for(i = 0; i < number_of_products; i++)
		pthread_mutex_init(&product_mutex[i], 0);

		
}

int main(){

	

	FILE *file;
	
	file = fopen("input.txt" , "r");
		
	/*-------------  Read informations from input file and fill necessary fields --------------*/	
	
	if(file != NULL){
		fscanf(file, "%d", &number_of_customers);		// take number of customers	
		
		fscanf(file, "%d", &number_of_sellers);			// take number of sellers	
		
		fscanf(file, "%d", &number_of_simulation_day);		// take number of simulation day

		fscanf(file, "%d", &number_of_products);		// take number of products
		

		

		customer_var_initialization();
		seller_var_initialization();
		product_var_initialization();
		

		// take number of each product and put it into products array
		int trash;
		int i;
		for( i = 0; i < number_of_products; i++ ){
			fscanf(file, "%d", &trash);
			products[i] = trash;
			available_products[i] = trash;
		}
		
		
		// take number of each product and put it into products array
		for( i = 0; i < number_of_customers; i++ ){
			int customer_id;
			fscanf(file, "%d", &customer_id);
			fscanf(file, "%d", &customer_informations[customer_id-1][0]);		// [i][0] keeps # of operations allowed
			fscanf(file, "%d", &customer_informations[customer_id-1][1]);		// [i][1] keeps # of reservable products
		}

	}
	else {
		printf("There is no file!");
	}
	fclose(file); 

	srand(time(0));	

	/*----------------------------------------------------------------------------------------------------------------*/
	

	// create therads
 	pthread_t customer_thread[number_of_customers];
    	pthread_t seller_thread[number_of_sellers];
    	long t;

	for ( t=0; t < number_of_customers; t++)
        	pthread_create(&customer_thread[t], NULL, customer, (void *)t);
    
    	for ( t=0; t < number_of_sellers; t++)
        	pthread_create(&seller_thread[t], NULL, seller, (void *)t);

	pthread_exit(0);



	
}
