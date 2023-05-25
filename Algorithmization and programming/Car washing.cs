using System;
using System.Collections.Generic;

class Program {
  
  public static void Main (string[] args) {
    Car car_1 = new Car("Lada","Vesta","Black");
    Car car_2 = new Car("Mitsubishi","Lancer X","White");
    Car car_3 = new Car("Hyundai","Solaris","Red");
    Car car_4 = new Car("Toyota","Starlet","Brown");
    Car car_5 = new Car("Toyota","Camry","Black");
    Car car_6 = new Car("Honda","Accord","Blue"); 
    
    Garage garage = new Garage();    
    CarWash wash = new CarWash();
    
    garage.addCar(car_1);
    garage.addCar(car_2);
    garage.addCar(car_3);
    garage.addCar(car_4);
    garage.addCar(car_5);
    garage.addCar(car_6);
    
    wash.WashAllCars(garage);    
  }
  
public class Car{
  public string Brand{get; set;}
  public string Model{get; set;}
  public string Color{get; set;}

  public Car(string brand, string model, string color){
    Brand = brand;
    Model = model;
    Color = color;
    
  }
  public void Wash()
    {
      Console.WriteLine($"{Brand} {Model} {Color} washed");
    }
  }

public class Garage{
  private List<Car> cars;
  
  public Garage(){
    cars = new List<Car>();
  }

  public void addCar(Car car){
    cars.Add(car);
  }

   public void RemoveCar(Car car){
    cars.Remove(car);
  }

  public void print(){
    foreach (Car car in cars){
      Console.WriteLine($"{car.Color} {car.Brand} {car.Model}");
    }
  }
  
  public List<Car> GetCars(){
    return cars;
  }
  
 }

public class CarWash{
  public void WashAllCars(Garage garage){
    foreach (Car car in garage.GetCars()){
      car.Wash();
    }
  }
}
}

