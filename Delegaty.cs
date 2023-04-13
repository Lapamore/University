using System;


interface IMath
{
    double Add(double a, double b);
    double Substract(double a, double b);
    double Multiply(double a, double b);
    double Divide(double a, double b);
}

class IMathClass : IMath
{
    public double Add(double a, double b)
    {
        return a + b;
    }

    public double Substract(double a, double b)
    {
        return a - b;
    }

    public double Multiply(double a, double b)
    {
        return a * b;
    }

    public double Divide(double a, double b)
    {
        return a / b;
    }
}

class Program
{

    delegate double MathOperation(double a, double b);

    static IMathClass iMathClass = new IMathClass();

    static void Main(){
    Console.WriteLine("Введите две цирфы:");
    var varChoose_1 = Convert.ToDouble(Console.ReadLine());
    var varChoose_2 = Convert.ToDouble(Console.ReadLine());
    MathOperation mathAction;
    Console.Write("Выберите операцию:");
    var choice = Console.ReadLine();
    mathAction = iMathClass.Add;
    Console.WriteLine(mathAction(varChoose_1, varChoose_2));
    switch (choice)
    {
    case "1":
      mathAction = iMathClass.Add;
      Console.Clear();
      Console.WriteLine($"Результат: {mathAction(varChoose_1, varChoose_2)}");
      break;
    case "2":
      mathAction = iMathClass.Substract;
      Console.Clear();
      Console.WriteLine($"Результат: {mathAction(varChoose_1, varChoose_2)}");
      break;
    case "3":
      mathAction = iMathClass.Multiply;
      Console.Clear();
      Console.WriteLine($"Результат: {mathAction(varChoose_1, varChoose_2)}");
      break;
    case "4":
      mathAction = iMathClass.Divide;
      Console.Clear();
      Console.WriteLine($"Результат: {mathAction(varChoose_1, varChoose_2)}");
      break;
    default:
      Console.WriteLine("Ошибка!");
      break;
    }
  }


}