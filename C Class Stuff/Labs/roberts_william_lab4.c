#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*William Riley Roberts
CSCI112 Lab 3
1/30/18
*/

int compute_grade_avg()
{
	//Instanciate all the floats (was having problems so started them as 0 to be safe)
	int numElements;
	float avg;
	float total;


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
	
	//Take the average of those values:
	for (int i = 0; i < numElements; ++i)
	{
		total += numberArray[i]; //Go through each spot in the array and add them up. 
	}
	avg = total/numElements;

	return(avg);

}

void write_grade_msg(int avg)
{
//Print out a message based on what avg the input grades had
	printf("Your average is: %d \n", avg);
	if (avg < 60)
	{
		printf("Failed semester - registration suspended\n", avg);
	}
	else if (avg >= 60 && avg <70)
	{
		printf("On probation for next semester\n", avg);
	}
	else if (avg >= 70 && avg < 80)
	{
		printf("(No message)\n");
	}

	else if (avg >= 80 && avg < 90)
	{
		printf("Dean's list for the semester\n", avg);
	}
	else
	{
		printf("Highest Honors for the semester\n", avg);
	}
}



int main()
{
	//run both compute and write grade:
	double avg = compute_grade_avg();
	write_grade_msg(avg);

	return(0);
}