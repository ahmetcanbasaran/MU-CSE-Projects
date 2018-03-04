/*
*   Sorts array A[0..n-1] by recursive mergesort
*   Input: An array A[0..n-1] of orderable elements
*   Output: Array A[0..n-1] sorted in nondecreasing order
*
*/

#include <iostream>

using namespace std;

int main(){

    int m = 0, n = 0, r = 0;

    cout << "Enter two nonnegative, not-both-zero integers: ";
    cin >> m >> n;

    while(n != 0){

        r = m % n;
        m = n; 
        n = r;

    }

    cout << "Great common divisor is: " << m << endl;

    return 0;

}