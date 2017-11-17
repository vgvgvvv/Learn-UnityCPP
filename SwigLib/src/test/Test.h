#ifndef __TEST__
#define __TEST__
#include "FooObject.h"

namespace SwigLibs
{
    class TestSwig
    {
    public:
        static int Add(int a, int b);
        int UseFool(FooObject* obj);
    };
}

#endif
