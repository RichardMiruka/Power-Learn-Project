// A map is a dynamic collection that represents 
// a set of values ​as key-value pairs.
// Keys and values ​in the map can be of any type 
// Maps are similar to dictionaries in python or objects in JavaScript.

void main() {
  //declaring map
  Map<String, int> marks = {
    "John": 90,
    "Doe": 80,
    "Smith": 70
  };

  //printing map
  print("Marks are $marks"); // Marks are {John: 90, Doe: 80, Smith: 70}

  //accessing elements
  print("John's marks are ${marks["John"]}");
  print("Doe's marks are ${marks["Doe"]}");
  print("Smith's marks are ${marks["Smith"]}");

  //adding elements
  marks["Alex"] = 85;
  marks["Alice"] = 95;

  print("Updated marks are $marks"); // Updated marks are {John: 90, Doe: 80, Smith: 70, Alex: 85, Alice: 95}
  
  //checking if an element exists in the map using containsKey method
  print(marks.containsKey("Alex")); // true
  print(marks.containsKey("John")); // true

  //removing elements from the map using remove method
  marks.remove("Doe");
  marks.remove("Smith"); 
  
  // removing multiple elements at once using removeWhere method
  marks.removeWhere((key, value) => value < 90);
  print("Removed marks are $marks"); // Removed marks are {John: 90, Alice: 95}

  //clearing the map using clear method
  marks.clear();
  print("Cleared marks are $marks"); // Cleared marks are {}

  //checking if the map is empty using isEmpty method
  print(marks.isEmpty); // true

  //getting the length of the map using length method of the map object
  print(marks.length); // 0

  //iterating over a map using forEach method of the map object
  marks.forEach((key, value){
    print("Key is $key and value is $value");
  }); // no output as the map is empty now

  /*
   * Map methods can also be used with other data types like int, double, bool, and list.
   */ 

  var numbers = {"one":1, "two":2, "three":3};
  numbers.addAll({"four":4, "five":5});
  print("Numbers map after adding all : $numbers"); // Numbers map after adding all : {one: 1, two: 2, three: 3, four: 4, five: 5}
  print("Numbers map after adding all ${numbers.length} elements"); // Numbers map after adding all 5 elements
  print("Numbers map after adding all ${numbers.isEmpty}"); // Numbers map after adding all false
  print("Numbers map ${numbers}"); // Numbers map {one: 1, two: 2, three: 3, four: 4, five: 5}

  var values = {"a":1, "b":2, "c":3};
  var keys = {"x":"a", "y":"b", "z":"c"};
  var result = <String,int>{};
  result.addEntries([MapEntry("x", 1), MapEntry("y", 2), MapEntry("z", 3)]);
  print("Result map ${result}"); // Result map {x: 1, y: 2, z: 3}

  List<int> numsList = [1, 2, 3, 4, 5];
  var sumOfNums = numsList.reduce((value, element) => value + element);
  print("Sum of numbers in the list is $sumOfNums"); // Sum of numbers in the list is 15 


  var dbls = {1.0, 2.0, 3.0, 4.0, 5.0};
  var avgDoubles = dbls.reduce((value, element) => value + element) / dbls.length;
  print("Average of doubles in the set is $avgDoubles"); // Average of doubles in the set is 3.0

  var bools = {true, false, true, false, true};
  var allTrue = bools.every((element) => element == true);
  print("Do all elements in the set are true? $allTrue"); // Do all elements in the set are true? false

  var anyFalse = bools.any((element) => element == false);
  print("Are there any false elements in the set? $anyFalse"); // Are there any false elements in the set? true
  print("Are there any false elements in the set? ${bools.any((element) => element == false)}"); // Are there any false elements in the set? true
  
}

