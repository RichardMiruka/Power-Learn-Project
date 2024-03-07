
 //In the next section, we will learn about the different types of functions in Dart. 
 //A function is a set of statements that performs a specific task.
 //In Dart, functions are objects and have a type, Function.
//Types of Functions in Dart 
//Dart supports the following types of functions: 
// 1. Named Functions 2. Anonymous Functions 3.Lambda Functions 

//Named Functions 
//A named function is a function that has a name.
// We have already seen an example of a named function in the previous section.
// 
  void add (int num1, int num2){
    print('Sum: ${num1 + num2}');
  }
  
//In the above code,  add  is the name of the function. 

// Anonymous Functions 
//An anonymous function is a function that does not have a name. 
  void main() {
    var add = (int num1, int num2) {
      print('Sum: ${num1 + num2}');
    };
    add(10, 20);
  }
  
//In the above code, we have created an anonymous function and assigned it to a variable  add.
// We then call the  add  function with two arguments  10  and  20 . 

// Lambda Functions 
//A lambda function is a concise way to write a function. 
  void maiin() {
    var add = (int num1, int num2) => print('Sum: ${num1 + num2}');
    add(10, 20);
  }
  
//In the above code, we have created a lambda function and assigned it to a variable  add .
// We then call the  add  function with two arguments  10  and  20 . 
//In the next section, we will learn about the parameters in Dart functions.


// Parameters in Dart Functions 
//Parameters are the variables that are used to pass data to a function. 
//Dart functions can have the following types of parameters: 
//Required Parameters Optional Parameters Default Parameters Named Parameters

 
//Required Parameters 
//Required parameters are the parameters that are mandatory to pass when calling a function. 
  void addd (int num1, int num2){
    print('Sum: ${num1 + num2}');
  }
  
// In the above code,  num1  and  num2  are required parameters.
// They must be provided while calling the function.
//add  takes two required integer parameters named  num1  and  num2 .

//Optional Parameters  
//Optional parameters allow you to provide default values to the parameters. 
//If no value is passed for these optional parameters while calling the function, the default value is used.
//Optional parameters allow you to provide default values to the parameters.  If no value is passed for these optional parameters while calling the function, the default value is used.
void multiply (int num1, int num2, [int num3 = 1]){
  print('Product: ${num1 * num2 * num3}');
}

// In the above code,  num3  is an optional parameter with a default value of  1 .
// It means that if no value is given for  num3  while calling the  multiply  function, the default value  1  will be used.


//Default Parameters 
//Default parameters are used if no argument is provided for the parameter. 
//They work like optional parameters but they are named. 
void subtract (int num1, int num2, {int num3 = 0}){
  print('Difference: ${num1 - num2 - num3}');
}

//Named Parameters  
//Named parameters are identified by their names  and can be passed in any order. 
void divide(int numerator, {int denominator = 1}){
  print('Result: ${numerator / denominator}');
}

//In the above code,  denominator  is a named parameter. It doesn't need to be passed explicitly;
// if not passed, it will take the default value  1 .

//In the next section, we will learn about the return type of functions in Dart. 
//A function's return type specifies the type of value that the function can return.  
//This helps us understand what kind of value the function will return. 
