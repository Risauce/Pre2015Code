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
	float first = 0;
	float second = 0;
	float third = 0;
	float fourth = 0;
	float fifth = 0;

	//Ask the user to input their 5 grades. 
	printf("Enter your five class grades seperated by spaces: ");
	scanf("%f %f %f %f %f", &first, &second, &third, &fourth, &fifth);
	
	//Take the average of those values:
	int avg = (first + second + third + fourth + fifth)/5;
	int result = ceil(avg); //Round that

	return(result);

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
