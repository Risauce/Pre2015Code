
#include <stdio.h>

/* Riley Roberts
 * Lab1, CSCI112
 * 1/19/18
 */

int main(void){
	double celsius;
	double fahrenheit;

	printf("Enter the temperature in Celsius: ");
	scanf("%lf", &celsius);
	fahrenheit =(celsius * 9/5 + 32);

	printf("Converted to Fahrenheit: %lf fahrenheit. \n", fahrenheit);

	return(0);
}


