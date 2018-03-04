/*
*           23.02.2018, Friday Night
*           Euclid's Great Common Divisor Algorithm
*           Author: Oğuzhan BÖLÜKBAŞ
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