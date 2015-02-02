#include "RIPEMD-160.h"

int main(int argc, char **argv)
{
   
        RIPEMD_160 gufrip;
    char fname[]="./text";
   if (!gufrip.read_file(fname))
            cout << "Ошибка чтения файла!" << endl << endl;
        gufrip.ripemd_160();
    return 0;
}