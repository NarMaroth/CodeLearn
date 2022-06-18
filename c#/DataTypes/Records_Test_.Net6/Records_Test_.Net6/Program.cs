
//------------
Record1 r1a = new(FirstName: "Jose", LastName: "Hernandez");

Console.WriteLine($"Record: {r1a.ToString()}");

var (fn, ln) = r1a; // pass values to variables
Console.WriteLine($"FirstName: {fn} LastName: {ln}");


//------------
// test con string y un entero
Record2 r2a = new(FirstName: "Maria", Age: 30);
var (name, age) = r2a;
Console.WriteLine($"FirstName: {name} Age: {age}");


//------------
Record1 r1b = r1a with
{
    FirstName = "Pepe"
};





//------------
// A Record is just a fancy class
// Los valores de un Record no se pueden cambiar, son como una clase ReadOnly
// Simple Record Declaration
public record Record1(string FirstName, string LastName);
public record Record2(string FirstName, int Age);


// class version of record declaration
public class Class1 
{

    public string FirstName { get; init; }
    public string LastName { get; init; }

    public Class1(string firstName, string lastName)
    {
        FirstName = firstName;
        LastName = lastName;
    }

    // var (fn, ln) = r1a; (esto se consigue gracias al deconstructor (No Destructor))
    public void Deconstruct(out string FirtsName, out string LastName) 
    {
        FirtsName = this.FirstName;
        LastName = this.LastName;
    }
}


//------------
// Record delcaration
public record Record3(string FirstName, String LastName) 
{
    private string _firtsName = FirstName;

    public string FirstName
    {
        get { return _firtsName.Substring(startIndex: 0, length: 1); }
        init { }
    }


    public string FullName { get => $"{FirstName} {LastName}"; }

    public string SayHello() 
    {
        return $"Hi i am {FirstName}";
    }
}



