%module opencv

%{
#define SWIG_FILE_WITH_INIT
#include "opencv.h"
%}

int detectAndDisplay(char* img);
