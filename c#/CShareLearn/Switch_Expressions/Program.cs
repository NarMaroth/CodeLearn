
using System;

double DoMath(double a, double b, MathType operation) 
{
    //Switch
    switch (operation) 
    {
        case MathType.Add:
            return a + b;
            break;
        case MathType.Subtract:
            return a - b;
            break;
        case MathType.Multiply:
            return a * b;
            break;
        case MathType.Divide:
            return a / b;
            break;
        default:
            throw new Exception("Bad info passed in");
    }

    //Switch Expression (C# 8.0)
    double output = 0;
    output = operation switch
    {
        MathType.Add => a + b,
        MathType.Subtract => a - b,
        MathType.Multiply => a * b,
        MathType.Divide => a / b,
        _ => throw new Exception("Bad info passed in");
    };
}

enum MathType {Add,Subtract,Multiply,Divide}
