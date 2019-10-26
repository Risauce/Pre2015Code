//This program is the first part of program2, and will read in the file and create 
//a binary file of the results. (Build the database)
//while not end of file:
//To read the file we will use fgets() to read the line and then strtok to parse


//To build the database we will create a structure, and then make an array of all 
//the structures together
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct //Define our main structure
{
	char name[20];
	int price;
	int aisle;
	char cat;
}item_t;

int main(int argc, char const *argv[])
{
	FILE *inFile = fopen("grocery.txt", "r");
	FILE *outFile = fopen("output.bin", "wb"); //Create the input and output files

	int iaisle, iprice;
	char icat;
	char iname[20];	

	item_t masterList[100]; //Create the master list

	int i =0;
	while(fscanf(inFile, "%s %d %d %c", iname, &iprice, &iaisle, &icat) != EOF) 
	{ //This reads the desired format until it hits EOF, and adds them to the data base
		
		strcpy(masterList[i].name, iname);
		masterList[i].price = iprice;
		masterList[i].aisle = iaisle;
		masterList[i].cat = icat;

		i++;
	}


	/*
	int n;
	for (n = 0; n < i; ++n)
	{
		printf("%s %d\n", masterList[n].name, masterList[n].price);
		//fprintf(outFile, "%s %d %d %c\n", masterList[n].name, masterList[n].price, masterList[n].aisle, masterList[n].cat);

	}
	*/
	fwrite(&masterList, sizeof(item_t), i, outFile); //Write the array of structures to the binary file

	fclose(inFile); //Close the files
	fclose(outFile);
	return 0;
}
