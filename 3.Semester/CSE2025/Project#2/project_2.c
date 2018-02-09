/*		
*		
*		2016/11/11 16:40 ___  -> ___  -> ___  -> ___  -> ___  -> ___  -> ___  -> ___ 2016/12/04 21:37
*
*		Oguzhan BOLUKBAS, 150114022, CSE 2023 - Data Structures Project2
*
*		This program, in the beginning, reads numbers from text file("input.txt") and inserts them to
*	2D Binary Search Tree. Using this program, you can add new values to the program, delete values from
*	the tree, print the three. It use recursive and nonrecursive functions to do that oportunities.
*
* 
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct BSTNode{

	short key1;
	short key2;
	short depth;	//To help print function
	struct BSTNode *lPtr;
	struct BSTNode *rPtr;

};

//Definning types
typedef struct BSTNode BSTNode;
typedef struct BSTNode *BSTNodePtr;

//Pointer of BST
BSTNodePtr BSTPtr = NULL;

//Pointer of a node which will be deleted
BSTNodePtr willDeleted = NULL;

int treeDepth = 0;
int searchTreeDepth = 0;
int treeDepthForPrint = 0;

//To help recursive delete function
int minDif = 1000;
int minKey1 = 1000;
int minKey2 = 1000;

//Prototypes of functions
void readFile();
void seperate();
void insert(int, int);
void printTree(BSTNodePtr* , int);
void searchTree(BSTNodePtr, int, int);
void deleteNode(BSTNodePtr, int, int);

int main(){
	
	char choice;	//To keep what the user want to do
	int key1, key2;
	
	printf("%s%s%s%s%s%s" , "Choose what do you want:\n\n",
			" 1 - Read an input file\n",
		 		" 2 - Enter new node\n",
					" 3 - Remove a node\n",
						" 4 - Print 2-d binary tree\n\n",
							"Enter q to exit\n\n");

	do {
		
		scanf("%c" , &choice);
		
		if(choice == '1'){
			
			readFile();
			
			printf("The input file has been read\n");
			
			
		} else if(choice == '2'){
			
			printf("Please enter new input's first key: ");
			scanf("%d" , &key1);
			
			printf("Please enter new input's second key: ");
			scanf("%d" , &key2);
						
			insert(key1, key2);
			
			printf("\nThe new node has been added\n\n");
			
			
		} else if(choice == '3'){
			
			printf("Please enter first key: ");
			scanf("%d" , &key1);
			
			printf("Please enter second key: ");
			scanf("%d" , &key2);
			
			deleteNode(BSTPtr, key1, key2);
			
			printf("\nThe node has been removed\n\n");		
			
		} else if(choice == '4'){
			
			int i = 0;
			int p = 0;			
			
			treeDepthForPrint = treeDepth;
			
			for(i = 0; i <= treeDepth; i++){
				
				for(p = treeDepth - i; p > 0; p--){
					
					printf("     ");
					
				}
				
				printTree(&BSTPtr, i);
				
				printf("\n");
				
			}
			
			treeDepthForPrint = 0;
			
			
		} else if(choice == '\n'){
			
			
		} else {
			
			printf("Wrong input!\n");
						
		}

		
	} while (choice != 'q');

	return 0;

}

//To read file from text file
void readFile(){
	
	char key[10];	//To keep character
	
	FILE *fPtr;		//File pointer
	
	//Print error if the file does not exist
	if((fPtr = fopen("input.txt" , "r")) == NULL){
		
		printf("File could not be found\n");
	
	//If we have a file	
	} else {
				
		do {
			
			fscanf(fPtr, "%s", &key);
			
			seperate(key);
			
		} while( !feof(fPtr) );
		
		fclose(fPtr);
		
	}
	
}

//Seperate line into two part and convert them to a number
void seperate(char input[10]){
	
	int num1 = 0;
	int num2 = 0;
	
	int c = 0;
	int i = 0;
	int k = 0;
	
	for(i = 0; i < 10; i++){
		
		printf("%c" , input[i]);
		
	}
	
	printf("\n");
	
	//For first part of line(key1)
	for(i = 0; i < 10; i++){
		
		//To check wheter it is a number
		if(input[i] >= '0' && input[i] <= '9'){
						
			num1 *= 10;
		
			num1 += input[i] - '0';
									
		} else {
			
			c++;
			
			break;
			
		}
		
		c++;	//Keep the beginning position of second number(key2)
				
	}
		
	//For second part of line(key2)
	for(k = c; k < 10; k++){
		
		//To check wheter it is a number
		if(input[k] >= '0' && input[k] <= '9'){
			
			num2 *= 10;
		
			num2 += input[k] - '0';
						
		}
		
		else{
			
			break;
			
		}
		
	}
		
	insert(num1, num2);		//Insert this two values to the BST
	
}

//To obtain two key and insert them to 2D BST
void insert(int key1, int key2){
	
	int depth = 0;		//To determine node's depth
	int inserted = 0;
	
	//For first addin(generating the root)
	if(BSTPtr == NULL){	
		
		depth = 0;
				
	} else {		
	
		depth = BSTPtr -> depth;		
		
	}	
	
	//Make a new node
	BSTNodePtr np = malloc(sizeof(BSTNode));
	np -> key1 = key1;
	np -> key2 = key2;
	np -> lPtr = NULL;
	np -> rPtr = NULL;
	
	//If it is, define it to root
	if(BSTPtr == NULL){
		
		np -> depth = depth;
		
		BSTPtr = np;
		
	} else {
				
		BSTNodePtr cPtr = BSTPtr; 	//To keep parent
		BSTNodePtr ncPtr = BSTPtr;	//To keep child
		
		while (inserted != 1){
						
			if(depth % 2 == 0){		//Look at first keys
								
				if(key1 < (cPtr -> key1)){
										
					ncPtr = ncPtr -> lPtr;
					
					//To add new node to left subtree of parent
					if(ncPtr == NULL){
						
						np -> depth = depth + 1;
												
						cPtr -> lPtr = np;
						
						inserted = 1;
					
					//If it has been deleted, rearrange the keys							
					} else if (ncPtr -> key1 == -1 && ncPtr -> key2 == -1){
						
						ncPtr -> key1 = key1; 
						ncPtr -> key2 = key2;
						
						return;
					
					//Continue	
					} else {
												
						cPtr = cPtr -> lPtr;
						
					}
					
				} else if(key1 > (cPtr -> key1) ){
										
					ncPtr = ncPtr -> rPtr;
					
					//To add new node to right subtree of parent
					if(ncPtr == NULL){
						
						np -> depth = depth + 1;
							
						cPtr -> rPtr = np;
						
						inserted = 1;
					
					//If it has been deleted, rearrange the keys							
					} else if (ncPtr -> key1 == -1 && ncPtr -> key2 == -1){
						
						ncPtr -> key1 = key1; 
						ncPtr -> key2 = key2;
						
						return;
					
					//Continue	
					} else {
												
						cPtr = cPtr -> rPtr;
						
					}
					
				}	//End of right subtree
				
			} 	//End of even depth
			
			//This algorithm similiar with depth % 2 = 0 algorithm			
			if(depth % 2 == 1){
				
				if(key2 < (cPtr -> key2) ){
										
					ncPtr = ncPtr -> lPtr;
					
					if(ncPtr == NULL){
						
						np -> depth = depth + 1;
												
						cPtr -> lPtr = np;
						
						inserted = 1;
												
					} else if (ncPtr -> key1 == -1 && ncPtr -> key2 == -1){
						
						ncPtr -> key1 = key1; 
						ncPtr -> key2 = key2;
						
						return;
						
					} else {
												
						cPtr = cPtr -> lPtr;
						
					}
					
				} else if(key2 > (cPtr -> key2) ){
										
					ncPtr = ncPtr -> rPtr;
					
					if(ncPtr == NULL){
						
						np -> depth = depth + 1;
												
						cPtr -> rPtr = np;
						
						inserted = 1;
												
					} else if (ncPtr -> key1 == -1 && ncPtr -> key2 == -1){
						
						ncPtr -> key1 = key1; 
						ncPtr -> key2 = key2;
						
						return;
						
					} else {
												
						cPtr = cPtr -> rPtr;
						
					}
					
				}	//End of right subtree
				
			}	//End of odd depth
						
			depth++;
			
			//Define max. depth of tree
			if(depth > treeDepth)
				treeDepth = depth;
						
		}	//End of while
		
	}	//End of else
	
}	//End of function

//Print the BST according to depths recursively
void printTree(BSTNodePtr *head_node, int depth){
	
    BSTNodePtr head;
    head = *head_node;
    
    int dp = depth;
    
	if(head == NULL && treeDepth == 0){
		
        printf("BST does not exist!\n");
        
		return;
    
	} else if (head == NULL){
		
		printf("x  ");
				
		return;	
	
	} else {
        
		if(head -> depth == dp && head -> key1 != -1){
			
			printf("%d,%d " , head -> key1, head -> key2);
        
    	} else {
    		
    		
    		
		}
    	
		printTree (&(head -> lPtr), dp);
        
		printTree (&(head -> rPtr), dp);
    
	}
    
}

//To search correct keys for deleted node in order to protect logic of BST
BSTNodePtr searchMin(BSTNodePtr root, int data, int depth){ 
				
	int difference = 0;				
	
	if(root == NULL){
						
		return;
	
	} else {
			 
		if(depth % 2 == 0){		//Check first keys
				
			//If keys are -1, do not check the difference
			if(root -> key1 == -1 && root -> key2 == -1){
								
				return;
				
			}
		
			//Get absolute value of difference
			difference = fabs((root -> key1) - data);
						
			//It is searchin node in order to delete	
			if(difference == 0){
				
				minKey1 = -1;
				minKey2 = -1;
			
			//Reaarange the node which hasa fit keys for deleting node position	
			} else if(difference < minDif){
								
				minDif = difference;
								
				minKey1 = root -> key1;
				minKey2 = root -> key2;
				
				willDeleted = root;
								
			}
			
			//Check left child
			if(root -> lPtr != NULL){
								
				searchMin(root -> lPtr, data, depth);
								
			}
			
			//Check right child
			if(root -> rPtr != NULL){
								
				searchMin(root -> rPtr, data, depth);
										
			}
			
		}
		
		//This algorithm has similiar logic design with depth % 2 = 0 algorithm
		if(depth % 2 == 1){
				
			if(root -> key1 == -1 && root -> key2 == -1){
								
				return;
				
			}
		
			difference = fabs((root -> key2) - data);
								
			if(difference == 0){
				
				minKey1 = -1;
				minKey2 = -1;
				
			} else if(difference < minDif){
								
				minDif = difference;
								
				minKey1 = root -> key1;
				minKey2 = root -> key2;
				
				willDeleted = root;
								
			}
						
			if(root -> lPtr != NULL){
								
				searchMin(root -> lPtr, data, depth);
								
			}
			
			if(root -> rPtr != NULL){
												
				searchMin(root -> rPtr, data, depth);
										
			}
			
		}
		
	}
		
}

//To delete the wanted node with finding correct new node recursively
void deleteNode(BSTNodePtr root, int data1, int data2){ 
	
	int depth = root -> depth;
	int founded = 0;
	
	BSTNodePtr p = root;
	
	
	//Delete it without checking new correct node
	if(root -> lPtr == NULL && root -> rPtr == NULL){
				
		root -> key1 = -1;
		root -> key2 = -1;

		return;
		
	} else {
	
		while(founded != 1){
						
			if(depth % 2 == 0){		//To check according to first keys
								
				//The node which is searching is founded		
				if(p -> key1 == data1 && p -> key2 == data2){
										
					//Find new correct node instead of deleting node					
					searchMin(p, p -> key1, p -> depth);
										
					//Rearrange keys					
					p -> key1 = minKey1;
					p -> key2 = minKey2;
										
					//To find new node for used node for deleted node
					if(willDeleted != NULL){
						
						minDif = 1000;
												
						deleteNode(willDeleted, minKey1, minKey2);
						
					}
					
					//Rearrange those to default values					
					minKey1 = 1000;
					minKey2 = 1000;
					
					founded = 1;
					
					break;
				
				//To check right child	
				} else if (data1 > p -> key1){
										
					if(p -> rPtr == NULL){
						
						printf("\nThe node cannot be founded\n\n");
												
						return;
						
					} else {
												
						p = p -> rPtr;
						
					}
				
				//To check left child	
				} else if (data1 < p -> key1){
										
					if(p -> rPtr == NULL){
						
						printf("\nThe node cannot be founded\n\n");
						
						return;
						
					} else {
												
						p = p -> lPtr;
						
					}
					
				}
				
			}
			
			//It has similiar logic with above
			if(depth % 2 == 1){
										
				if(p -> key1 == data1 && p -> key2 == data2){
															
					searchMin(p, p -> key2, p -> depth);
															
					p -> key1 = minKey1;
					p -> key2 = minKey2;
																				
					if(willDeleted != NULL){
						
						minDif = 1000;
												
						deleteNode(willDeleted, minKey1, minKey2);
						
					}
										
					minKey1 = 1000;
					minKey2 = 1000;
					
					founded = 1;
					
					break;
					
				} else if (data2 > p -> key2){
					
					if(p -> rPtr == NULL){
						
						printf("\nThe node cannot be founded\n\n");
						
						return;
						
					} else {
						
						p = p -> rPtr;
						
					}
					
				} else if (data2 < p -> key2){
					
					if(p -> rPtr == NULL){
						
						printf("\nThe node cannot be founded\n\n");
						
						return;
						
					} else {
						
						p = p -> lPtr;
						
					}
					
				}
				
			}	//End of if
						
			depth++;
			 
		}	//End of while	
		
	}	//End of else
			
}
