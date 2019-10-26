#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*William Riley Roberts
CSCI112 Program 1
2/12/18

This program asks the user to input how many numbers they want entered, then to enter that many numbers
It then takes the average, finds the max, and finds the min; printing them out.
*/


void calculateAvg(float array[], int n)
{
	float avg, total; 

	int i;
	for (i = 0; i < n; ++i)
	{
		total += array[i]; //Go through each spot in the array and add them up. 
	}

	avg = total/n;
	printf("\nThe Average of those numbers is %f \n", avg);

}

void getSmallest(float array[], int n)
{
	float smallest = 999999999999; //Get the biggest number possible, so everything is smaller than it

	for (int i = 0; i < n; ++i)
	{
		if (array[i] < smallest)
		{
			smallest = array[i]; //If any number is found to be smaller, make that the new smallest
		}
	}

	printf("The smallest number given is %f \n", smallest);


}

void getBiggest(float array[], int n)
{
	float biggest = 0; //Start with 0, so any number is bigger

	for (int i = 0; i < n; ++i)
	{
		if (array[i] > biggest)
		{
			biggest = array[i]; //If anything in the array is found bigger, then that is the new biggest
		}
	}

	printf("The biggest number given is %f \n", biggest);

}

int main(int argc, char const *argv[])
{
	int numElements;


	printf("How many numbers are you entering?\n");
	scanf("%d", &numElements); //this is n
	while (numElements <= 0) //An array can't have less than 1 position
	{
		printf("That is an invalid number, retry.\n");
		scanf("%d", &numElements);

	}

	float numberArray[ numElements ]; //Create an array with specified number of elements

	for (int i = 0; i < numElements; i++)
	{
		printf("Number %d?: \n", i); //As the user to fill the array
		scanf("%f", &numberArray[i]);
	}

	for (int i = 0; i < numElements; ++i)
	{
		printf("%.1f ", numberArray[i]); //print out the array for clarifying purposes
	}

	calculateAvg(numberArray, numElements);
	getSmallest(numberArray, numElements); //run all the methods
	getBiggest(numberArray, numElements);


	return 0;
}