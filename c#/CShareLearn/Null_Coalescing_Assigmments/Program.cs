// Depending if the prop was initialize in the class contructor it will give an error if is
// used. To avoid that and  having to write and if statement to checking if is null,
// we use the Null Coalescing Assigmments (??=).

var example = new ListDemo();

// If luckyNumber is null, generate list, else do nothing.
example.LuckyNumber ??= new List<int>();

example.LuckyNumber.Add(15);

foreach (var number in example.LuckyNumber) 
{
    Console.WriteLine(number);
}

class ListDemo
{
    public List<int> LuckyNumber { get; set; }

    //public ListDemo()
    //{
    //    LuckyNumber = new List<int>();
    //}
}
