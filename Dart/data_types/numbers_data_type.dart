void main() {
  // Declaring Variables
  int num1 = 100; //without decimal point or whole number
  double num2 = 3.14; //with decimal point or fractional part
  num num3 = 150; // num can store both int and double
  num num4 = 73.4; // num can store both int and double with decimals

//Printing info
//print(Num 1 is $num1); output is not supported in dartpad, so running on local IDE 
//print(Num 2 is $num2); output is not supported in dartpad, so running on local IDE 
//print(Num 3 is $num3);
//print(Num 4 is $num4);
  
  //For Sum
  num sum = num1 + num2 + num3 + num4;
  print("Sum of numbers is ${sum}" );
   
//For Subtraction
  int diff = (num1 - num2).toInt();
  print("\nDifference between num1 and num2 is $diff");
  
  //For Multiplication
  num product = num1 * num2 * num3 * num4;
  print("Product of numbers is ${product}");

//For Division (Returns double)
  double quotient = num1 / num2;
  print("\ndivision of num1 and num2 is $quotient");
  
//For Modulus (Returns int)
  int remainder = (num1 % num2).toInt();
  print("\nRemainder when num1 is divided by num2 is $remainder");
  
/* Increment & Decrement */
  ++num1;     // Postfix Increment
  --num2;     // Postfix Decrement
  print("\nPostfix incremented value of num1 is $num1");
  print("Postfix decremented value of num2 is $num2");
  
  num1++;      // Prefix Increment
  num2--;       // Prefix Decrement
  print("\nPrefix incremented value of num1 is $num1");
  print("Prefix decremented value of num2 is $num2");
  
 /* Assignment Operators */
  num1 += 50;  // num1 = num1 + 50
  num2 -= 10.5;  // num2 = num2 - 10.5
  num3 *= 2;  // num3 = num3 * 2
  num4 /= 2; // num4 = num4 / 2
  print("\nValue after addition assignment operator is $num1");
  print("Value after subtraction assignment operator is $num2");
  print("Value after multiplication assignment operator is $num3");
  print("Value after division assignment operator is $num4");
  
  /* Relational operators */
  if(num1 > num2){
    print("\n$num1 is greater than $num2");
  }
  else{
    print("\n$num1 is less than $num2");
  }
  
  if(num1 == num2){
    print("$num1 is equal to $num2");
  }
  else{
    print("$num1 is not equal to $num2");
  }
  
  if(num1 != num2){
    print("$num1 is not equal to $num2");
  }
  else{
    print("$num1 is equal to $num2");
  }
}

