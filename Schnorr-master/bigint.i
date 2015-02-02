%module bigint
%{
/* Includes the header in the wrapper code */
#include "bigint.h"
%}

%include "std_vector.i"
%include "std_string.i"

%rename(st) operator string;
%rename(_in) operator >>;
%rename(_out) operator <<;

%nestedworkaround bigint::divzero;

/* Parse the header file to generate wrappers */
%include "bigint.h"