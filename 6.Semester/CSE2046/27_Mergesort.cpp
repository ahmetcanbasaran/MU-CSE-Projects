/*
*   Sorts array A[0..n-1] by recursive mergesort
*   Input: An array A[0..n-1] of orderable elements
*   Output: Array A[0..n-1] sorted in nondecreasing order
*
*/

#include <iostream>
#include <Math.h>

using namespace std;

void copy_array(int source[], int dest[], int beginning){

    int size = sizeof(A)/sizeof(*A) - beginning;
	int dest_c = 0; // Counter for destination array
    int src_c = beginning; // Counter for source array 

	for(src_c = 0; src_c < size; src_c++, dest_c++){

		dest[dest_c] = src[src_c];

	}

}

int mergesort(int A[]){

    if (n > 1) {

        int length_A = sizeof(A) / sizeof(*A);

        int B[floor(length_A/2) - 1];
        int C[ceil(length_A/2) - 1];

        copy_array(A, B, 0);
        copy_array(A, C, floor(length_A/2));

        mergesort(B);
        mergesort(C);
        
        merge(B, C, A)

    }

}

int main(){

    const size_t max_size = 100;
    int A[max_size] = {};
    
    cout << "Enter integers('x' to stop)\n";
    
    size_t size = 0;
    
    while(cin >> A[size++] && size < max_size)
        ; //Empty loop body
    
    cin.clear(); //Clear failed state
    cin.ignore(); //Discard first symbol in stream (our X)

    Mergesort(A);

    return 0;

}