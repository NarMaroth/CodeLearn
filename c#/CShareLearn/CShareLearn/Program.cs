using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO; //Added

namespace CShareLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            //Output
            Console.WriteLine("Hello_World");

            Console.WriteLine("num1 = {0}, num2 = {1}", 100, 200);

            //Input
            string name = Console.ReadLine();
            Console.WriteLine(name);

            int num = Convert.ToInt16(Console.ReadLine());
            Console.WriteLine("You number is: {0}", num+num);
            Console.ReadLine();

            // multidimensional arrays
            int[,] x = new int[3, 4];

            // array of arrays
            int[][] jaggedArr = new int[3][];
            /* or
               int[ ][ ] jaggedArr = new int[ ][ ] 
                {
                  new int[ ] {1,8,2,7,9},
                  new int[ ] {2,4,6},
                  new int[ ] {33,42}
                };
            */

            int[] arr = { 2, 4, 7 };

            Console.WriteLine(arr.Length); // prints the arr lenght

            Console.WriteLine(arr.Rank); // prints the numbers of dimensions

            // Arr.Sum() returns the sum of all the element in the array

            Console.WriteLine(DateTime.Now);
            Console.WriteLine(DateTime.Today);
            Console.WriteLine(DateTime.DaysInMonth(2021,6));

            // Errors
            try
            {
                int[] arr2 = new int[] { 4, 5, 8 };
                Console.Write(arr[8]);
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Lol dont divide by 0 moron");
            }
            catch (Exception e)
            {
                Console.WriteLine("An error occurred:{0}", e.Message);
            }
            finally {
                //exdcute if there was an error or not
            }

            // create fila and add the string to it;
            string str = "Some text";
            File.WriteAllText("test.txt", str);
        }

        void Test(ref int num) {
            // pasar por referencia solo sirve con variables inicializadas
        }

        // int num = 1;
        // Test(num);

        /*
        void Test2(out int num) {
            // mismo pero para variables sin inicialziar
        }
        */

        // int num;
        // Test2(out num);

        // Generic Class
        class Stack<T>
        {
            int index = 0;
            T[] innerArray = new T[100];
            public void Push(T item)
            {
                innerArray[index++] = item;
            }
            public T Pop()
            {
                return innerArray[--index];
            }
            public T Get(int k) { return innerArray[k]; }
        }

    }
}
