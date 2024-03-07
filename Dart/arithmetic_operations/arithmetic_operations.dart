// Arithmetic operators are the most common types of operators.
// They perform operations like addition, subtraction, multiplication, division.

void main() {
  int a = 10;
  int b = 20;

  // Addition
  print('Addition: ${a + b}'); // Output: 30

  // Subtraction
  print('Subtraction: ${a - b}'); // Output: -10

  // Multiplication
  print('Multiplication: ${a * b}'); // Output: 200

  // Division
  print('Division: ${a / b}'); // Output: 0.5 (returns a double)

  // Modulus
  print('Modulus: ${a % b}'); // Output: 10 (returns the remainder of the division)

  // Increment and Decrement Operators
  // The increment operator (+=) adds 1 to the variable.
  // The decrement operator (-=) subtracts 1 from the variable.
  a += 5; // a = a + 5
  print('Incremented Value: $a'); // Output: 15

  b -= 7; // b = b - 7
  print('Decremented Value: $b'); // Output: 13

  // Compound Assignment Operators
  // These operators combine an assignment operation with an arithmetic operation.
  // Example: x += y is equivalent to x = x + y.
  a <<= 2; // a = a << 2 (left shift by 2 bits)
  print('Left Shift: $a'); // Output: 60

  b >>= 4; // b = b >> 4 (right shift by 4 bits)
  print('Right Shift: $b'); // Output: 0x0f (Output: 15 in hexadecimal)

  // Bitwise AND Operator (&)
  int c = 9; // 1001 in binary
  int d = 5; // 0101 in binary
  print('Bitwise AND: ${c & d}'); // Output: 1 (0001 in binary)

  // Bitwise OR Operator (|)
  print('Bitwise OR: ${c | d}'); // Output: 13 (1101 in binary)

  // Bitwise XOR Operator (^)
  print('Bitwise XOR: ${c ^ d}'); // Output: 12 (1100 in binary)

  // Ternary If-Else Operator
  int e = 7;
  String f = (e == 7) ? 'Yes' : 'No';
  print("Is 7 equal to 7? $f"); // Output: Yes
}