using System;
using System.Linq;
using System.Collections.Generic;

class Program {
  public static void Main (string[] args) {
		Random rnd = new Random();
		rnd.Next();
		
		List<Driver> Drivers = new List<Driver>();
    Drivers.Add(new Driver("Лещёв Дмитрий Евгеньевич"));
		Drivers.Add(new Driver("Зензин Егор Николаевич"));
		Drivers.Add(new Driver("Сагалбаев Дамир Амангельдыевич"));
		Drivers.Add(new Driver("Лапиков Максим Вячеславович"));

		List<CarModel> CarTypes = new List<CarModel>();
		CarTypes.Add(new CarModel("Nissan Sunny 2001"));
		CarTypes.Add(new CarModel("Mitsubishi Lancer 2015"));
		CarTypes.Add(new CarModel("Lada Granta 2022"));
		CarTypes.Add(new CarModel("Lada Vesta 2020"));
		CarTypes.Add(new CarModel("BMW M8 Gran Coupe 2023"));
		CarTypes.Add(new CarModel("BMW X5 2023"));

		List<Car> CarList = new List<Car>();
		
		for(int _ = 0; _ < rnd.Next(5, 10); _++){
			Car Car = new Car(IDGen(), Convert.ToString(rnd.Next(1, 86)), "RUS", CarTypes[rnd.Next(CarTypes.Count)]);
			CarList.Add(Car);
			for(int __ = 0; __ < rnd.Next(1, 2); __++){
				Drivers[rnd.Next(Drivers.Count)].AddCar(Car.ID);
			}
		}
		Drivers[rnd.Next(Drivers.Count)].AddCar(CarList[rnd.Next(CarList.Count)].ID);
		
		foreach(var i in Drivers){
			Console.WriteLine(i.name);
			foreach(var j in i.Owns){
				Console.WriteLine(j);
			}
		}

		Console.WriteLine();
		string temp = CarList[rnd.Next(CarList.Count)].ID;
		Console.WriteLine($"Владельцы автомобиля {temp}");
		var ChosenByCar = from i in Drivers where i.Owns.Contains(temp) select i.name;
		foreach(var i in ChosenByCar) Console.WriteLine(i);

		Console.WriteLine();
		char letter = 'Л';
		Console.WriteLine($"Водители с фамилией на букву {letter}");
		var DriversNameStartWith = from i in Drivers where i.name.Split()[0][0] == letter select i.name;
		foreach(var i in DriversNameStartWith) Console.WriteLine(i);
  }

  public class CarModel{
		string name {get;}

		public CarModel(string name){
			this.name = name;
		}
	}
	
	public class Car{
		public string ID {get;}
		string region;
		string country;
		public CarModel model;

		public Car(string ID, string region, string country, CarModel model){
			this.ID = ID;
			this.region = region;
			this.country = country;
			this.model = model;
		}
	}
	
	public class Citizen{
		public string name; 

		public Citizen(string name){
			this.name = name;
		}
	}
	public class Driver : Citizen{
		public List<string> Owns = new List<string>();
		
		public Driver(string name) : base(name) {}

		public void AddCar(string id){
			Owns.Add(id);
		}
	}
	public static string IDGen(){
		Random rnd = new Random();
		string alpha = "ABCEHKMOPTX";
		string id = "";
		id = Convert.ToString(rnd.Next(0, 10)) + Convert.ToString(rnd.Next(0, 10));
		for (int i = 0; i<3; i++){
			id = id + alpha[rnd.Next(alpha.Length)];
		}
		id += Convert.ToString(rnd.Next(0, 10));
		return id;
	}
}
