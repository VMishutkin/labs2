#include "md5_lite.h"

int main()
{
	assert(sizeof(byte)==1 && sizeof(dword)==4 && sizeof(dword64)==8);
                                                               
	char fname[]="./text";
    char *mas= MD5().ifopen(fname);
 



	byte res[16];
printf("Hash for %s\n",mas);
	MD5::install();
	MD5 md5;
	md5.update(mas);
	md5.final(res);
	
}