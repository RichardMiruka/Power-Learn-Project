// String helps you to store text data in your program.
// You can use single or double quotes to store string in dart.

void main() {
  //Declaring a variable
  String schoolName = "Power Learn Project";
  String courseName = 'Dart Programming';
  String address = "Nairobi, Kenya";
  String website = 'www.powerlearn.com';
  String email = "info@powerlearn.com";

  print("School Name: $schoolName");
  print("Course Name: $courseName");
  print("Address: $address");
  print("Website: $website");
  print("Email: $email");
}

/* Output will be :
School Name: Power Learn Project
Course Name: Dart Programming
Address: Nairobi, Kenya
Website: www.powerlearn.com
Email: info@powerlearn.com */

// String helps you to store text data in your program.
// In the above example we have declared and initialized 5 variables of type String.
// To display these values we used print function and used $ sign to display the value of the variable.
// So when you run this code it will display the value of the variables as shown in the output.

// Note that if you want to add a string to another string, you can use the + operator.

String fullName(String firstName, String lastName) {
  return firstName + " " + lastName;
}

void main1() {
  String name = fullName("John", "Doe");
  print(name);
} /* Output will be : John Doe */</dart> 

//In the above example we created a function fullName which takes two parameters firstName and lastName of type String.
// This is an example how you can pass parameters to a function in dart.
// Here we created a new function named fullName which takes two parameters firstName and lastName of type String.
// Inside the function we used + operator to concatenate the two strings and returned the result.
// Then in the main method we called the fullName function and passed two strings "John" and "Doe" as parameters.
// The function returned the concatenated string and we stored it in a variable name and then printed it. 
// So when you run this code it will display the concatenated string as shown in the output.


// You can also assign the return value of a function to a variable of type String.
// In the above example we created a function fullName which takes two parameters firstName and lastName of type String.
void main2() {
  String name = fullName("John", "Doe");
  print(name);
} /* Output will be : John Doe */  
 //In the above example we created a function fullName which takes two parameters firstName and lastName of type String.

 // Here we created a new class School with a constructor which takes 4 parameters.
class School {
  String schoolName;
  String courseName;
  String address;
  String website;

  School(this.schoolName, this.courseName, this.address, this.website);
}

void main3() {
  School school = new School("Power Learn Project", "Dart Programming",
      "Nairobi, Kenya", "www.powerlearn.com");
  print("School Name: ${school.schoolName}");
  print("Course Name: ${school.courseName}");
  print("Address: ${school.address}");
  print("Website: ${school.website}");
} /* Output will be :
    School Name: Power Learn Project
    Course Name: Dart Programming
    Address: Nairobi, Kenya
    Website: www.powerlearn.com */ 

//In the above example we created a new class School with properties schoolName, courseName, address and website
// and a constructor which takes 4 parameters.
void main4() {
  School school = new School("Power Learn Project", "Dart Programming",
      "Nairobi, Kenya", "www.powerlearn.com");
  print("School Name: ${school.schoolName}");
  print("Course Name: ${school.courseName}");
  print("Address: ${school.address}");
  print("Website: ${school.website}");
} /* Output will be :
    School Name: Power Learn Project
    Course Name: Dart Programming
    Address: Nairobi, Kenya
    Website: www.powerlearn.com */ 

//In the above example we created a new class School with a method called displayDetails(). This method prints out the details of the school.
// The `toString()` method is called when an object is printed using the print() function.
void main5() {
  School school = new School("Power Learn Project", "Dart Programming",
      "Nairobi, Kenya", "www.powerlearn.com");
  print(school);
} /* Output will be :
    School Name: Power Learn Project
    Course Name: Dart Programming
    Address: Nairobi, Kenya
    Website: www.powerlearn.com */
