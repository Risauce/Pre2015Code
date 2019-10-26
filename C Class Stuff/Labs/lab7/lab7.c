#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Class
{
	char *name;
	char *id;
	int credits;
};

int main(int argc, char const *argv[])
{
	char theLine[100];
	char copyLine[100];

	struct Class allClasses[8];

	char *iid, *nname, *cred;
//---------------------------------------------
	//Gather all the data from the file and stick it in structures in an array
	int i;
	while(1)
	{
		fgets(theLine, 100, stdin);

		strcpy(copyLine, theLine);
   		   		
		iid = malloc(10 * sizeof(char));
		strcpy(iid, strtok(theLine, " "));

		nname = malloc(60 * sizeof(char));
		strcpy(nname, strtok(NULL, "1234")); //Grab all the values from the string
		
		cred = &copyLine[strlen(copyLine)-2];
		int ccred = *cred - '0';

		if (strcmp(iid, "XXXXXXX") == 0) //This marks the end of the file
		{
			break;
		}

		allClasses[i].id = iid;
		allClasses[i].name = nname;
		allClasses[i].credits = ccred;

		i++;

}
//-------------------------------------------------
	//Print out all the information
	int totalCredits = 0;	
	int totalCScred = 0;
	int totalCSclass = 0;

	int n; //This will get the total num of classes (this is the same value as i)
	for (n = 0; n < i; ++n) //Try and print out all the array values. Gets the cred but not the id or name.
	{
		printf("Class: ID-%s Name-%s Credits-%d\n", allClasses[n].id, allClasses[n].name, allClasses[n].credits);
		totalCredits += allClasses[n].credits;
		if (strncmp(allClasses[n].id, "CSCI", 4) == 0) //If the first 4 char of the ID are CSCI, then add
		{
			totalCSclass += 1;
			totalCScred += allClasses[n].credits;
		}
	}
	printf("Total Classes: %d\nTotal Credits: %d\nCSCI Classes: %d\nCSCI Credits: %d\n", n, totalCredits, totalCSclass, totalCScred);

//--------------------------------------------------
	free(iid);
	free(nname);
	return 0;
}