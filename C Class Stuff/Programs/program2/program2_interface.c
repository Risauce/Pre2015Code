//Second program of our assignment
//include masterlist.h
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct
{
	char name[20];
	int price;
	int aisle;
	char cat;
}item_t;


//UserInterface(ml, numItems);


void addToMasterList(item_t *ml, int *numItem)
	{
		char iname[20];
		int cost, iaisle;
		char icat;

		printf("Enter the name cost aisle and category separated by spaces\n");
		scanf("%s %d %d %c", iname, &cost, &iaisle, &icat);

		strcpy(ml[*numItem].name, iname);
		ml[*numItem].price = cost;
		ml[*numItem].aisle = iaisle;
		ml[*numItem].cat = icat;

		*numItem += 1;
	}

void printCatNumber(item_t *ml, int *numItems) //This function prints out how many of the requested category there are
{
	char category;
	printf("Which category?\n");
	scanf(" %c", &category);

	int sum = 0;
	int i;
	for (i = 0; i < *numItems; ++i) //Count up how many there are,
	{
		if (category == ml[i].cat)
		{
			sum++;
		}
	}

	printf("There are %d items in the ", sum); //Then print out how many and which category
		switch(category)
		{
			case 'C':
				printf("Canned Goods");
				break;
			case 'M':
				printf("Meat");
				break;
			case 'D':
				printf("Dairy");
				break;
			case 'P':
				printf("Produce");
				break;
			
			default:
				printf("Invalid Category");
		}

		printf(" Category\n" );
		
}

void printList(item_t *ml, int *numItems) //This function prints out each category's items.
{
	int i, j;
	char cats[] = {'C', 'D', 'M', 'P'};
	for (i = 0; i < 4; ++i)
	{
		switch(cats[i])
		{
			case 'C':
				printf("\nCanned Goods");
				break;
			case 'M':
				printf("\nMeat");
				break;
			case 'D':
				printf("\nDairy");
				break;
			case 'P':
				printf("\nProduce");
				break;
			
			default:
				printf("Invalid Category");
		}
		printf(" Category\n");
		for (j = 0; j < *numItems; ++j)
		{
			if (ml[j].cat == cats[i])
			{
				printf("%s %d %d %c\n", ml[j].name, ml[j].price, ml[j].aisle, ml[j].cat);
				
			}
		}
	}
}

void userInterface(item_t *ml, int *numItems) //This is the pivotal function, it controls
{ //what the user inputs, and calls the other functions based on their input.
	char option = 'A';
	
	printf("Choose an option;\n A(Add to List), N(print cat number), L(Print entire List), X(Quit)");
	while(option != 'X')
	{
		printf("\nWhat is your choice?\n");
		scanf(" %c", &option);
		switch(option)
		{
			case 'a':
			case 'A':
				addToMasterList(ml, numItems);
				break;
			case 'n':
			case 'N':
				printCatNumber(ml, numItems);
				break;
			case 'l':
			case 'L':
				printList(ml, numItems);
				break;
			case 'x':
			case 'X':
				break;
			default:
				printf("Illegal Option\n");
		}
	}
}

	
int main(int argc, char const *argv[])
{
	
	item_t masterList[100];
	
	FILE *inFile = fopen("output.bin", "rb"); //Initialize the reaading file

	int numItems = fread(masterList, sizeof(item_t), 100, inFile); //Read the file to masterlist
	printf("Number of items is: %d\n", numItems);

	//flcose binary file
	fclose(inFile);

	userInterface(masterList, &numItems); //Run UserInterface
	

	return 0;
}

