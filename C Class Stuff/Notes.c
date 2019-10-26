#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Practice done in class:
//CCreate a structure for a location
//It will have lat/lon degrees, minutes, direction

struct Lat
{
	float degrees;
	int min;
	char direction;
};

struct Lon
{
	float degrees;
	int min;
	char direction;
};

struct Location
{
	struct Lat p1;
	struct Lon p2;
	
};

// How she did it----
/*
typedef struct {
	int degrees;
	int min;
	char dir;

}latLon_t;

typedef struct{
	latLon_t lat;
	latLon_t lon;
}location_t;
*/
//-------------------


int main()
{
	//---------------------------
	/*
	location_t mor;
	mor.lat.degrees = 45;
	mor.lat.min = 6;
	mor.lat.dir = 'N';

	mor.lon.degrees = 111;
	mor.lon.min = 4;
	mor.lon.dir = 'W';
	*/
	//--------------------------
	struct Location mor = {{45, 6, "N"}{111, 4, "W"}}
}


