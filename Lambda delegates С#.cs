using System;
class Program{
    delegate double Operation(double x, double y, double z);
    public static class Operations{
      public static double minimal(double x, double y, double z){
        Func<double, double, double, double> min = (double x, double y, double z) => Math.Min(x, Math.Min(y,z));
        return min(x, y, z);
      }

      public static double maximum(double x, double y, double z){
        Func<double, double, double, double> max = (double x, double y, double z) => Math.Max(x, Math.Max(y,z));
        return max(x, y, z);
      }

      public static double summa(double x, double y, double z){
        Func<double, double, double, double> sum = (double x, double y, double z) => x+y+z;
        return sum(x, y, z);
      }

      public static double averege(double x, double y, double z){
        Func<double, double, double, double> avg = (double x, double y, double z) => (x+y+z)/3;
        return avg(x, y, z);
      }

      public static double multiply(double x, double y, double z){
        Func<double, double, double, double> mul = (double x, double y, double z) => x*y*z;
        return mul(x, y, z);
      }
      
    }
    static void Main()
    {
      Operation min = new Operation(Operations.minimal);
      Operation avg = new Operation(Operations.averege);
      Operation mul = new Operation(Operations.multiply);
      Operation sum = new Operation(Operations.summa);
      Operation max = new Operation(Operations.maximum);
      Console.WriteLine("Введите три цирфы:");
      var varChoose_1 = Convert.ToDouble(Console.ReadLine());
      var varChoose_2 = Convert.ToDouble(Console.ReadLine());
      var varChoose_3 = Convert.ToDouble(Console.ReadLine());
      Console.Write("\nВыберите операцию:\n1. Сумма\n2. Минимальное\n3. Максимальное\n4. Произведение\n5. Среднее значение\n");
      var choice = Console.ReadLine();
      switch (choice)
      {
      case "1":
        Console.Clear();
        Console.WriteLine($"Результат: {sum(varChoose_1,varChoose_2,varChoose_3)}");
        break;
      case "2":
        Console.Clear();
        Console.WriteLine($"Результат: {min(varChoose_1,varChoose_2,varChoose_3)}");
        break;
      case "3":
        Console.Clear();
        Console.WriteLine($"Результат: {max(varChoose_1,varChoose_2,varChoose_3)}");
        break;
      case "4":
        Console.Clear();
        Console.WriteLine($"Результат: {mul(varChoose_1,varChoose_2,varChoose_3)}");
        break;
      case "5":
        Console.Clear();
        Console.WriteLine($"Результат: {avg(varChoose_1,varChoose_2,varChoose_3)}");
        break;
      default:
        Console.WriteLine("Ошибка!");
        break;
      }
    }
  }
  
  
