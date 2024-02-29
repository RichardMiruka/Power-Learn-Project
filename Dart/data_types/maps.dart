// A map is a dynamic collection that represents 
// a set of values ​as key-value pairs.
// Keys and values ​in the map can be of any type 

void main() {
  //declaring map
  Map<String, int> marks = {
    "John": 90,
    "Doe": 80,
    "Smith": 70
  };

  //printing map
  print("Marks are $marks");

  //accessing elements
  print("John's marks are ${marks["John"]}");
  print("Doe's marks are ${marks["Doe"]}");
  print("Smith's marks are ${marks["Smith"]}");

  //adding elements
  marks["Alex"] = 85;
  marks["Alice"] = 95;

  print("Updated marks are $marks");
}