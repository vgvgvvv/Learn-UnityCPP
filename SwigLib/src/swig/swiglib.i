%module swiglib
%include "std_vector.i"
%include "std_string.i"
%include "cpointer.i"
%include "carrays.i"

%{

#include "../test/Test.h"
#include "../test/FooObject.h"

%}

%include "../test/Test.h"
%include "../test/FooObject.h"

namespace std {

%template(BoolVector) vector<bool>;
%template(Fooector) vector<FooObject>;

};

%pointer_class(bool, BoolPointer);
%array_class(unsigned char, UnsignedCharArray);
%array_class(int, IntArray);