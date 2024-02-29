void main() {
  //declaring variables
  String name = "dart class";
  int age = 76;
  double price = 100.14;
  var year = 2024;
  num students = 460;

  //printing variables using print function

  print(name); //printing name variable value
  print("Age is $age");//printing age variable value with string concatenation
  print('Price is ${price.toStringAsFixed(2)}');//printing price variable value with string concatenation and formatting the number to two decimal places
  print('Price is $price');//printing price variable value with string concatenation without formatting
  print("Year is ${year + 1}");//printing year variable value with string concatenation and adding 1 to it
  print("Number of Students are ${students - 10}");//printing students variable value with string concatenation and subtracting 10 from it
  print(age);
  print(price);
  print(year);
  print(students);
}
