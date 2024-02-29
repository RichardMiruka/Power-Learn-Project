// String helps you to store text data in your program.
// You can use single or double quotes to store string in dart.

void main() {
  //Declaring a variable
  String schoolName = "Power Learn Project";
  String courseName = 'Dart Programming';
  String address = "Nairobi, Kenya";
  String website = 'www.powerlearn.com';
  String email = "info@powerlearn.com";

  //Printing info about the School
  print("School Name: $schoolName");
  print("Course Name: $courseName");
  print("Address: $address");
  print("website : $website");
  print("email: $email");
  print(
      "Welcome to $schoolName, we offer $courseName in $address. For more info, visit our website $website or email us at $email.");
  print(
      "You just joined $schoolName to pursue $courseName. It is located in $address. For more infor, visit our website $website or email us at $email");
}
