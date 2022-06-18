



var stopWatch = System.Diagnostics.Stopwatch.StartNew();
ExecuteSync();
stopWatch.Stop();

var stopWatch2 = System.Diagnostics.Stopwatch.StartNew();
await ExecuteAsync();
stopWatch2.Stop();

var stopWatch3 = System.Diagnostics.Stopwatch.StartNew();
await ParallelExecuteAsync();
stopWatch3.Stop();
Console.WriteLine($"Sync:{stopWatch.ElapsedMilliseconds} / Async:{stopWatch2.ElapsedMilliseconds} / ParellelAsync:{stopWatch3.ElapsedMilliseconds}");

// ------------------------------------
// Keep track of Async Task

Progress<str_ProgressReport> progress = new();
progress.ProgressChanged += OnResourceLoaded;
ExecuteAsyncWithProgress(progress);

// ------------------------------------
// Task Cancelation

CancellationTokenSource cancellation = new();

Progress<str_ProgressReport> progress2 = new();
progress.ProgressChanged += OnResourceLoaded;

ExecuteAsyncWithProgressAndCancelation(progress2,cancellation.Token);

//The code below shoud stop the taks above. This wont work bc, it will wait until the Mehtod ends and then cancel it.
cancellation.Cancel();

//--------------------------------------

void ExecuteSync() 
{
    TheMethod();
}
void TheMethod()
{
    for (int i = 0; i < 100000; i++)
    {
        Console.WriteLine("Hi i am mr.methods");
    }
}

// dont declare the function return as void, return Task insted.
async Task ExecuteAsync()
{
    for (int i = 0; i < 10000; i++)
    {
        await Task.Run(() => PrintMessage());
    }
}

void PrintMessage()
{
    Console.WriteLine("Hi am an Sync Method");
}


// ----------------------------------------
// Insted of waiting to end the task and then start another, all task are added to a list  as there are created
// and then we wait for all of them to finish.
async Task ParallelExecuteAsync()
{
    List<Task> tasks = new List<Task>();
    for (int i = 0; i < 10000; i++)
    {
        tasks.Add(Task.Run(() => PrintMessage()));
    }

    await Task.WhenAll(tasks); 
}


// ----------------------------------------
// This is a !!!Sync!!! Method where the method PrintName its execute multiple times in parallel by using Parallel.ForEach
void ParallelExecute()
{
    List<string> nombres = new() {"Pepe","Juan","Arnaldo","Racarazaece"};
    Parallel.ForEach<string>(nombres, (nombre) =>
    {
        PrintName(nombre);
    });
}
void PrintName(string nombre)
{
    Console.WriteLine($"Hi am {nombre}");
}

// ----------------------------------------
// This is the Async version of the code above.
async Task ParallelExecuteAsinc()
{
    List<string> nombres = new() { "Pepe", "Juan", "Arnaldo", "Racarazaece" };

    await Task.Run(() => {
        Parallel.ForEach<string>(nombres, (nombre) =>
        {
            PrintName(nombre);
        });
    });
}


// ----------------------------------------
// Keeping track of the async operation with IProgress and IProgress.Report()
async Task ExecuteAsyncWithProgress(IProgress<str_ProgressReport> progress)
{
    str_ProgressReport report = new();
    int iterations = 10000;
    for (int i = 1; i <= iterations; i++)
    {
        await LoadResource();
        report.percentageCompleted = (i * 100) / iterations;
        progress.Report(report);
    }
}

async Task LoadResource() 
{
    Console.WriteLine("Loading Resource Method");
}

void OnResourceLoaded(object? sender, str_ProgressReport e)
{
    Console.WriteLine($"{e.percentageCompleted}% Resources Loaded. Updating progressbar status");
}


// ----------------------------------------
// Cancel Task if requested
async Task ExecuteAsyncWithProgressAndCancelation(IProgress<str_ProgressReport> progress, CancellationToken cancellationToken)
{
    str_ProgressReport report = new();
    int iterations = 10000;
    for (int i = 1; i <= iterations; i++)
    {
        // 1. If a cancellation is requested
        if (cancellationToken.IsCancellationRequested) 
        {
            // set up task end on cancellation
        }

        // 2. Throws an exeption (OperationCanceledException) to stop the task, if a cancellation is requested
        cancellationToken.ThrowIfCancellationRequested();
        
        await LoadResource();
        report.percentageCompleted = (i * 100) / iterations;
        progress.Report(report);
    }
}

struct str_ProgressReport
{
    public float percentageCompleted { get; set; }
}
