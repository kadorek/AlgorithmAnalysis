using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecursiveDicFib
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine(Fib(5));
            Console.ReadLine();

        }


        static int Fib(int n, Dictionary<int, int> dict = null)
        {
            Dictionary<int, int> d = new Dictionary<int, int>();
            if (dict != null)
            {
                d = dict;
            }
            if (n == 1 || n == 2)
            {
                d.Add(n, 1);
                return Fib(n, d);
            }
            else
            {
                d.Add(n)
            }

            if (d.Keys.Contains(n - 1))
            {
                return d[n - 1] + d[n - 2];
            }
            return Fib(n - 1, d);



        }




    }
}
