
var places = new string[] {"First","Second","Third","Fourth","Fifth" };


Console.WriteLine($"The last item in the list is {places[^1]}");

Console.WriteLine();

Console.WriteLine("Places from pos 2 to pos 3");
foreach (var place in places[2..4]) 
{
    Console.WriteLine(place);
}

Console.WriteLine("Places from pos 2 to the place before the last position");
foreach (var place in places[2..^1])
{
    Console.WriteLine(place);
}


Console.WriteLine("Every place exept the las one");
foreach (var place in places[..^1])
{
    Console.WriteLine(place);
}

Console.WriteLine("Every place from pos 1");
foreach (var place in places[1..])
{
    Console.WriteLine(place);
}