// In this function, you do pass the parameter and also expect return type
// in this function, we add two numbers
int add(int a, int b) {
  int sum = a + b;
  return sum;
}

// main function / running application
void main() {
  int num1 = 30;
  int num2 = 20;
  int total = add(num1, num2); // calling the add() function with parameters
  print('The sum is $total'); // printing the result
}

// In this program, int add(int a, int b) is the function with int as the return type,
// and the pair of parenthesis has two parameters, i.e., a and b.