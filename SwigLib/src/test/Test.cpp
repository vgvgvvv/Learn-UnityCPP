#include "Test.h"

namespace SwigLibs
{
    int TestSwig::Add(int a, int b)
    {
        return a + b;
    }


    int TestSwig::UseFool(FooObject* obj)
    {
        return obj->a;
    }
};