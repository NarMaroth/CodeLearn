// TEMPLATES

// Templates fuction/clase are only created or "Exists" if theyr called

template<typename T>
void someFunc(T value,T value2)
{
    if(value2 < value)
    {
        cout<<value<<endl;
    }
}

// depending of the type of the arguments that are entered, the function
// will be writen replacing the template types with the corresponding argumen type



template<int size>
class Array
{
    int array[size];

};

// because its not writen until it called you can define the size of an array

template<typename Type,int size>
class Array
{
    Type array[size];

};

