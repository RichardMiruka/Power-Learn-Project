void main() { // main function
   // list of cars
   List cars = ["BMW", "Toyota", "Mercedes", "Lexus", "Audi"];

   // iteration with anonymous function as a parameter
    cars.forEach((car) {
      print(car); // prints each car in the list one by one
    });
}