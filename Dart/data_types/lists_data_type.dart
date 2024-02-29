// Dart List is similar to an array,
// which is the ordered collection of the objects.
// If you want to store multiple values without 
// creating multiple variables, you can use a list

void main() {
  //declaring list
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //printing list
  print("numbers are $numbers");
  print("names are $names");
  print("isMarried are $isMarried");
}

/*
Output:
numbers are [1, 2, 3, 4, 5]
names are [John, Doe, Smith]
isMarrid are [true, false, true]
*/

// Accessing elements in the list
void accessElementsInList(){
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //accessing elements
  print("First number is ${numbers[0]}");
  print("Second name is ${names[1]}");
  print("Third isMarried is ${isMarried[2]}");
}

// Adding element to the existing list
void addElementToList() {
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //adding elements
  numbers.add(6);
  names.add("Alex");
  isMarried.add(false);

  //printing list
  print("numbers are $numbers");
  print("names are $names");
  print("isMarried are $isMarried");
}

// Removing elements from the list
void removeFromTheList() {
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //removing elements
  numbers.remove(3);
  names.remove("Doe");
  isMarried.remove(true);

  //printing list
  print("numbers are $numbers");
  print("names are $names");
  print("isMarried are $isMarried");
}

//Updating an Element in a List
void updateElementInList() {
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //updating elements
  numbers[0] = 10;
  names[1] = "Alex";
  isMarried[2] = false;

  //printing list
  print("numbers are $numbers");
  print("names are $names");
  print("isMarried are $isMarried");
}