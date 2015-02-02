#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <time.h>

#include "stribog.h"
#include <iostream>
using namespace std;

int main()
{
	printf("vvedite stroky\n");	
	char istr[256];
	cin >> istr;

	unsigned char h512[64]={}, h256[32] = {};

	hash_256(istr,strlen(istr),h256);
	//printf("%s",h256);
	printf("\n\n");
	hash_512(istr,strlen(istr),h512);
	//printf("%s",h512);
	return 0;
}
