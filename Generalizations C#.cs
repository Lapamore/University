using System;

class Program {
  public static void Main (string[] args) {
    Mylist<int> mylist = new Mylist<int>();
    
    mylist.Add(1);
    mylist.Add(2);
    mylist.Add(3);
    mylist.Add(4);
    mylist.Add(5);
    
    mylist.Del(5);
    Console.WriteLine(mylist[1]);
    
    for (int i = 0; i < mylist.Count; i++){
      Console.WriteLine(mylist[i]);
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
