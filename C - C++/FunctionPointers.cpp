#include <iostream>


void(*functPointerVarName)(int);

//1      2         3

//1 return type of the function
//2 create a variable pointer that it going to point towards the function
//3 the funtion parameters


void printHelloWorld()
{
    std::cout<<"HelloWorld"<<std::endl;
}

int printVar(auto var)
{
    std::cout<<"Var: "<<var<<std::endl;
    return 0;
}

void ForEach(const auto arr[], auto(*fun)(auto))
{
    for(auto value : arr)
    {
        fun(value);
    }
}

int main()
{
    auto res = printHelloWorld(); //with parentesis your calling the function and returning the result of it

    auto func = printHelloWorld;  // Without them its a pointer towards the function definition on the binary  
    // ==
    auto func = &printHelloWorld;    
    // ==
    void(*func)() = printHelloWorld;    // the function pointer type must have the same function return type and parameters

    // Example:

    int(*printVarFunc)(auto) = printVar;
    printVarFunc("Hola");
    printVarFunc(100);


    // Simplier Def:

    typedef int(*printVarFunc)(auto)    
    printVarFunc = printVar;

    printVarFunc("Hola");
    printVarFunc(100);


    // Usage Example
    int values[] = {1,2,3,4,5,6};
    ForEach(values, printVar);

    return 0;
}