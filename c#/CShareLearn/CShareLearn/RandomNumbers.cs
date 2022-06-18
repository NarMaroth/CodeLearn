using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CShareLearn
{
    internal class RandomNumbers
    {
        Random random = new Random();

        int IntRandomNumber() 
        {
            // Resturns a random number, based on the random seed.
            return random.Next(); 
        }

        double DoubleRandomNumber()
        {
            // Resturns a random double number between 0 and 1. Example: 0.9274213
            return random.NextDouble();

            // if you multiply NextDouble by 10 you will get a random number between 0 and 10
            //return random.NextDouble()*10;
        }



        struct Person 
        {
            public string firstName;
            public string lastName;
        }

        // we use Linq to order the list by picking a random number, then the person will be positioned by the number it got.
        void ShufleListByRandom(List<Person> people) 
        {
            people.OrderBy(x => random.Next());
        }

    }
}
