/*William Riley Roberts
 * CSCI 112 Lab 2 
 * 1/26/2018
 * Made with VIM
 */

#include <stdio.h>
#include <math.h>

int get_next(int previous, int current){
//This function takes in the previous term and the current term and returns the next term in // the sequence.
	double powered = pow(2, (current-1));
	return((powered*3) + previous);
}



void print_result(int final)
{
//This simple function just prints an int in a specific way. 
	printf("The number requested in the sequence is %d \n", final);
}





int main()
 {
//This is the main function of the program, and simply calls the get_next function above for each value in the sequence we desire. Particularily we went until we reached x5, and then
//passed that value into our custom print function. 
	int x1 = get_next(0, 1);
	int x2 = get_next(x1, 2);
	int x3 = get_next(x2, 3);
	int x4 = get_next(x3, 4);
	int x5 = get_next(x4, 5);//final sequence value needed

	print_result(x5); //print it
	return(0);
 }
