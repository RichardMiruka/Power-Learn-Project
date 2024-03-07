// Task 1
// Task 1: Function to add two numbers
int addTwo(int a, int b) {
  int sum = a + b;
  return sum;
}

// Task 2: function to subtract two numbers
int subtractTwo(int a, int b) {
  int difference = a - b;
  return difference;
}

// Task 3: function to multiply two numbers
int multiplyTwo(int a, int b) {
  int product = a * b;
  return product;
}

// Task 4: function to divide two numbers and handle division by zero error
double divideTwo(int a, int b) {
  if (b != 0) {
    return 0;
  } else {
    throw 'Cannot divide by zero';
  }
}

//Task 5: function that takes an argument of type String and returns lenth of the string
int stringLength(String str) {
  return str.length;
}

//Task 6: function that takes a list as an argument and returns the first element of that list
String getFirstElement(List<String> list) {
  return list[0];
} 

// main function / running application
void main() {
  // calling the functions with parameters and printing the result

  print('The sum is ${addTwo(30, 20)}'); // output: The sum is 50
  print('The difference is ${subtractTwo(30, 20)}'); // output: The difference is 10
  print('The product is ${multiplyTwo(30, 20)}'); // output: The product is 600
  print('The quotient is ${divideTwo(30, 20)}'); // output: The quotient is 1.5
  print('The length of the string is ${stringLength('Hello World')}'); // output: The length of the string is 11
  print('The first element of the list is ${getFirstElement(['apple', 'banana', 'cherry'])}'); // output: The first element of the list is apple
}
