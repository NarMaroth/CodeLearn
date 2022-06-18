
// Old Way -------------------
using (var inputFile = new StreamReader(@"D:\Demo\TestFile.txt")) 
{
    using (var outputFile = new StreamWriter(@"D:\Demo\OutputFile.txt")) 
    {
        string line;
        while ((line = inputFile.ReadLine()) is not null)
        {
            outputFile.WriteLine(line);
        }
    }
}

// New Way (C# 8.0) -----------
// Insted of declaring the scope with the using, the scope will be where its implemented the using. If is a method
// the stream will be close when you leave the method.

using var inputFile2 = new StreamReader(@"D:\Demo\TestFile.txt");
using var outputFile2 = new StreamWriter(@"D:\Demo\OutputFile.txt");

string line2;
while ((line2 = inputFile2.ReadLine()) is not null)
{
    outputFile2.WriteLine(line2);
}