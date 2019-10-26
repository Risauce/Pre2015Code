#include <stdio.h>


//Selection Sort---------------------------
typedef enum{false, true} bool;

void swap(char *a, char *b) //Swaps the two entered values in a list
{
	char store = *a;
	*a = *b;
	*b = store;
}

void selectionSort(char arr[], int size)//Adapted selection sort
{
	int i, j;
	for (i = 0; i < size; i++)
	{
		for (j = i; j < size; j++)
		{
			if (arr[i] < arr[j] && arr[j]) //Compares lexicographical values.
			{
				swap(&arr[i], &arr[j]);
			}
		}
	}
}

//------------------------------------------

/*
int compare(const void * a, const void * b)
{
	//Compare the strings by dereferencing them
	return strcmp(*(const char **)a, *(const char **)b);

}
*/

void print(char array[], int size)//Print an array with given size
{
	int i;
	for (i = 0; i < size; ++i)
	{
		printf("%c ", array[i]);
	}
	printf("\n");
}

void readToArr(char *array, int *counter)
{
	*counter = 0;
	char temp;
	bool ending = false;
	while(ending == false)
	{
		scanf("%c", &temp); //Read in one line
		if (temp == '0') //If its zero, stop
		{
			ending = true;
		}
		else if(temp != '\n') //Else, put it in the pointed-to array
		{
			array[*counter] = temp;
			*counter += 1;
		}

	}

}

int main(int argc, char const *argv[]) //There were many different ways of solving
//this, and I tried them all because my selection sort's 2nd nested for loop
//had a i++ instead of j++, always raising a segfault. So fun, it took me over an
//hour to realize it. True story of misery.

{
	//char buffer[BUFFERSIZE];
	int counter;
	int size = 26;
	char sortArray[size];

	/*
	while(fgets(buffer, BUFFERSIZE, stdin) != 0)
	{
		counter += 1;
		
		unsortArray[counter] = (int)buffer[0];
	}
	*/
	
	readToArr(sortArray, &counter); //Read in and apply all the values from the file
	selectionSort(sortArray, counter);//Sort it based on alphabetical values
	print(sortArray, counter);//Print it out

	//qsort(unsortArray, size, sizeof(const char *), compare); // THIS SHOULD WORK 

	return 0;
}