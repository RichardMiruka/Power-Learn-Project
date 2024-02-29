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
  print("isMarried is $isMarried");
}

/*
Output:
numbers are [1, 2, 3, 4, 5]
names are [John, Doe, Smith]
isMarried is [true, false, true]
*/

// Accessing elements in the list
void accessElementsInList(){
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //accessing elements
  print("First number is ${numbers[0]}"); // index 0
  print("Second name is ${names[1]}"); // index 1
  print("Third isMarried is ${isMarried[2]}"); // index 2
}

// Adding element to the existing list
void addElementToList() {
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> names = ["John", "Doe", "Smith"];
  List<bool> isMarried = [true, false, true];

  //adding elements
  numbers.add(6); //adding 6 at last position of numbers list
  names.add("Alex"); // adding Alex at last position of names list
  isMarried.add(false); // adding false at last position of isMarried list

  print("Updated numbers are $numbers");
  print("Updated names are $names");
  print("Updated isMarried are $isMarried");

  //adding multiple elements at once
  numbers.addAll([7,8,9]);
  names.addAll(["Jane", "Alice"]);
  isMarried..addAll([true, false]); // using .. operator for shorthand property notation

  print("\nAfter adding all elements at once");
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