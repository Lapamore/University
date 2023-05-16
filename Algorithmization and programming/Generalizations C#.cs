using System;

class Program {
  public static void Main (string[] args) {
    Mylist<int> mylist_int = new Mylist<int>();
    Mylist<string> mylist_string = new Mylist<string>();
    
    mylist_int.Add(1);
    mylist_int.Add(2);
    mylist_int.Add(3);
    mylist_int.Add(4);
    mylist_int.Add(5);

    mylist_string.Add("MO-221");
    mylist_string.Add("FIT-221");
    mylist_string.Add("FIT-222");
    mylist_string.Add("TMO-202");
    mylist_string.Add("ИВT-202");

    
    mylist_int.Del(5);
    Console.WriteLine(mylist_int[1]);
    
    for (int i = 0; i < mylist_int.Count; i++){
      Console.Write($"{mylist_int[i]}, ");
    }
    
    Console.WriteLine();

    mylist_string.Del("MO-221");
    Console.WriteLine(mylist_string[1]);
    
    for (int i = 0; i < mylist_string.Count; i++){
      Console.Write($"{mylist_string[i]}, ");
    }
    
  }
public class Mylist<T>
  {
    private T[] _array = Array.Empty<T>();

    public T this[int index]
    {
      get
      {
        return _array[index];
      }

      set
      {
        _array[index] = value;
      }
    }

    public int Count{get{return _array.Length;}}

    public void Add(T value)
    {
      var newArray = new T[_array.Length+1];
      for (int i = 0; i < _array.Length; i++)
      {
        newArray[i] = _array[i];
      }

      newArray[_array.Length] = value;
      _array = newArray; 
    }

    public void Del(T value)
    {
      int index = Array.IndexOf(_array, value);
      if (index > -1)
      {
          T[] newArray = new T[_array.Length - 1];
          for (int i = 0, j = 0; i < _array.Length; i++)
          {
              if (_array[i].Equals(value))
                  continue;

              newArray[j++] = _array[i];
          }
          _array = newArray;
      }
    }
  }
}
