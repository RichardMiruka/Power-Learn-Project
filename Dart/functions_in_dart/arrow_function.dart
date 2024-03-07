// If you want to declare a function in one line and it has only one expression,
// you can use the arrow function (=>) syntax.<s>This is called an arrow function.</s>
//The function is represented by => symbol.
// The arrow function is a shorthand syntax for writing functions in Dart.
// It consists of two parts: the parameter list and the function body.
// The parameter list is enclosed in parentheses and the function body is enclosed in curly braces.
// The arrow function is used to define a function that has only one expression.

// function that calculates interest without arrow function
double calculateInterest(double principal, double rate, double time) {
  double interest = principal * rate * time / 100;
  return interest;
}

void main() {
  double principal = 10000;
  double time = 2;
  double rate = 5;

  double result = calculateInterest(principal, rate, time);
  print('The interest is $result');
  
  // You can also write the above function using arrow function as shown below:
  /*print(*/'The interest is ${calculateInterest(principal, rate, time)}'/*)*/;
}
