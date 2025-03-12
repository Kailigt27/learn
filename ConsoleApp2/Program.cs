using System;
using System.Collections.Generic;
using System.Linq;
public class Program
{
    public static void Main()
    {
        List<int> list = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        var result = list.Where(x => x % 2 == 0).ToList();
        foreach (var item in result)
        {
            Console.WriteLine(item);
        }
    }
}