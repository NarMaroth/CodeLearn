using System.Threading; //  ImplicitUsings enabled (.net core 6.0)


Thread mainThread = Thread.CurrentThread;

mainThread.Name = "Main Thread";

Console.WriteLine("Main Thread Started");

Thread countdownThread = new Thread(CountDown);
Thread countupThread = new Thread(CountUp);
Thread messagesThread = new Thread(() => TenTimesMessages("Hola Mundo")); // para pasar parametros

countdownThread.Start();
countupThread.Start();
messagesThread.Start();

Console.WriteLine("Main Thread Completed");


void CountDown() 
{
    for (int i = 10; i > 0; i--)
    {
        Console.WriteLine("Countdown: " + i);
        Thread.Sleep(500);
    }
}

void CountUp()
{
    for (int i = 0; i < 10; i++)
    {
        Console.WriteLine("Countup: " + i);
        Thread.Sleep(1000);
    }
}

void TenTimesMessages(string message) 
{
    for (int i = 0; i < 10; i++)
    {
        Console.WriteLine("Message: " + message);
        Thread.Sleep(1000);
    }
}