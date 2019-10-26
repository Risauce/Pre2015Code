#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef enum{false, true} bool;

void palindrone(char *array)
{
	//printf("Got here!\n");
	int pos = 0;
	int l = strlen(array) - 1;
	int n = l + 1;

	while(pos < l)
	{
		//we compare each end of the string, if they are same, compare the next two inward
		if (array[pos++] != array[l--])
		{
			printf("String %s is not a palindrone\n", array);
			printf("Its first character is %c \n", array[0]);
			printf("It is of length %d\n", n);
			return;
		}
	}
	printf("%s is a palindrone\n", array);
	printf("Its first character is %c \n", array[0]);
	printf("It is of length %d\n", n);

}

void upperLower(char array[])
{
	int upper = 0;
	int lower =0;
	int i;
	int count = strlen(array);

	for (i=0; i < count; ++i)
	{
		if (array[i] >= 'A' && array[i] <= 'Z') //If the ASCI is between these, it is a capital
		{
			upper += 1; 
		}

		if (array[i] >= 'a' && array[i] <= 'z')//Likewise for lowercase.
		{
			lower += 1;
		}
		
	}
	printf("The number of Uppercase letters is %d\n", upper);
	printf("The number of Lowercase letters is %d\n", lower);

}

void isNumber(char array[])
{
	int is = 0;
	int i = 0;

	int hasDecimal = 0;
	int isInteger = 0;
	int isNumber = 0;


	while(i < strlen(array)) //Go unti end of array,
	{
		is = isdigit(array[i]); //Use the function to find if the value is a digit
		if (is == 0) 
		{
			isInteger = 0;
			//printf("The string is not an integer.\n");
			if (array[i] == '.')
			{
				hasDecimal += 1;
				isNumber = 1;
			}
			else 
			{
				isNumber = 0;
				isInteger = 0;
				//printf("The string is not a number.\n");
				break;
			}
			
		}
		else //If the number came back true for every spot in the string, it is  an int
		{
			isInteger = 1;
			//printf("The string is an integer\n");

		}
		i++;

	}
	if (isInteger == 1 && hasDecimal == 0) //Print based on what the above algorithm got
	{
		printf("The string is an integer.\n");
	}
	else
	{
		if (isNumber == 1 && hasDecimal <= 1)
		{
			printf("The string is a number, but not an integer.\n");
		}
		else
		{
			printf("The string is not a number.\n");
		}
	}
	
}


int main(int argc, char const *argv[])
{


	char *token;
	char line;
	int counter = 0;
	//const char s[2] = " ";

	while(counter < 2) //Scanf twice, 
	{
		scanf("%s", &line);
		printf("Got inside while\n");
		token = strtok(&line, " ");

		printf("%s\n", token);

		while(token != NULL)
		{
			printf("Got inside second while\n");
			int i;
			for (i= 0; i < 5; ++i)
			{
				palindrone(token);
				upperLower(token);
				isNumber(token);
				token = strtok(NULL, " ");

			}

		}
			counter++;

	}

/*
	palindrone("abba");
	palindrone("Nope");

	upperLower("aBBa");
	upperLower("Nope"); //It works will ALL of these. I just couldn't get strtok to work.
	upperLower("nope");

	isNumber("200");
	isNumber("38.38");
	isNumber("Anna");
	isNumber("30.93.92");
	*/

	return 0;
}