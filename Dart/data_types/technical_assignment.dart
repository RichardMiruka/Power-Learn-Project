void main() {
  // example of int data type 
  int year = 2024;
  print("The year is $year");
  
  // example of double data type
  double pi = 3.14;
  print("Value of PI is ${pi}");

  // example of string data type
  String greeting = "Goodmorning James!";
  print(greeting);

  // example of boolean data type - true or false
  bool isMale = true;
  print("Is he male? $isMale");
  
  // example of list data type  
  List<String> cities = ["Nairobi", "Kisumu", "Mombasa", "Nakuru"];
  print("Cities in Kenya are  ${cities}");

  // example of map data type
  Map<String, int> population = {
    "Nairobi": 4397000,
    "Kisumu": 968909,
    "Mombasa": 1208333,
    "Nakuru": 570674
  };
  print("Population of Nakuru is ${population["Nakuru"]}");
}
