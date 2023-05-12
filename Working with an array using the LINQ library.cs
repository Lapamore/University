using System;
using System.Linq;
class Program {
  public static void Main (string[] args) {
    int[] numbers = { 1, 2, 3, -1, -2, -3, 6, 3, 5, -2, 5, 10, 21, 34, 5};

    var numbers_greater_than_zero = from p in numbers where p>=0 select p; 

    var numbers_less_than_zero = from p in numbers where p < 0 select p;

    var even_numbers = from p in numbers where p % 2 == 0 select p;

    Console.WriteLine($"The number of positive numbers in the array: {numbers_greater_than_zero.Count()}");
    Console.WriteLine($"The number of negative numbers in the array: {numbers_less_than_zero.Count()}");
    Console.WriteLine($"The product of nonzero: {multiply(numbers_greater_than_zero.ToArray())}");
    Console.WriteLine($"The sum of even numbers: {even_numbers.Sum()}");
  }

  static public int multiply(int[] array_for_multiplication){
    int mul = 1;
      
    foreach (int i in array_for_multiplication){
      if (i > 0) mul*=i;
    }
    return mul;
  }
}
