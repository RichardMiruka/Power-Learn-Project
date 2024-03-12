/* eslint-disable project */

// The Array object, as with arrays in other programming languages,
// enables storing a collection of multiple items under a single variable name,
// and has members for performing common array operations.

// The Array object is a global object and can be used directly.
var arr = [1, 2, 3, 4, 5]; // An example of an array declaration
console.log(arr[0]); // 1 - Accessing the first element of the array (arrays are zero-indexed) // console.log(arr[0]) returns 1.

// Methods available on the Array object are:
// push() - Add one or more elements to the end of an array and returns the new length of the array.
// pop() - Remove the last element from an array and returns that element. If the array is empty, it returns undefined.
arr.push("Hello", "World"); // Add "Hello" and "World" to the end of the array // arr.push("Hello", "World") returns 7
console.log(arr); // ["1", "2", "3", "4", "5", "Hello", "World"]

// pop() - Remove the last element from an array and returns that element. If the array is empty, it returns undefined.
arr.pop(); // Remove the last element from an array and returns that element
console.log(arr); // ["1", "2", "3", "4", "5", "Hello"]

// shift() - Remove the first element from an array and returns that element. If the array is empty, it returns undefined.
arr.shift(); // Removes the first element from an array and returns that element. If called on an empty array it will return undefined.
console.log(arr); // ["2", "3", "4", "5", "Hello"] - Shows that the original order was not changed
                 // but only the last element ("Hello") was removed


// unshift() - Add one or more elements to the beginning of an array and returns the new length of the array.
arr.unshift("Hello", "World");
console.log(arr); // ["Hello", "World", "2", "3", "4", "5", "Hello"] - Shows that the original order was not changed
console.log(arr); // ["Hello", "World", "2", "3", "4", "5", "Hello"] - Shows that the original order was not changed

// slice() - Extracts a section of an array and returns a new array. It does not modify the original array.
var slicedArr = arr.slice(1, 3); // Extracts the second and third elements of the array
console.log(slicedArr); // ["World", "2"]

// splice() - Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.
console.log(arr); // ["Hello", "World", "2", "3", "4", "5", "Hello"] - Original array remains intact

// splice() - Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.
arr.splice(2, 2, "Goodbye", "Cruel", "World"); // Removes the third and fourth elements and replaces them with "Goodbye", "Cruel", "World"
console.log(arr); // ["Hello", "World", "Goodbye", "Cruel", "World", "4", "5", "Hello"] - Shows that the original array was modified

// concat() - Returns a new array comprised of this array joined with other array(s) and/or value(s).
var arr2 = ["Hello", "World"];
var mergedArr = arr.concat(arr2);
console.log(mergedArr); // ["Hello", "World", "Goodbye", "Cruel", "World", "4", "5", "Hello", "Hello", "World"]

// join() - Joins all elements of an array into a string.
var str = arr.join(", ");
console.log(str); // "Hello, World, Goodbye, Cruel, World, 4, 5, Hello"

// indexOf(), lastIndexOf() - Returns the first (last) index at which a given element can be found in the array, or -1 if it is not present.
// indexOf(), lastIndexOf() - Returns the first (last) index at which a given element can be found in the array, or -1 if it is not present.
// indexOf() - Returns the first index at which a given element can be found in the array, or -1 if it is not present.

console.log(arr.indexOf("Hello")); // 0 - "Hello" is the first element of the array
console.log(arr.lastIndexOf("Hello")); // 7 - "Hello" is the last element of the array

// reverse() - Reverses the order of the elements of an array in place. The first array element becomes the last, and the last array element becomes the first.
if (arr.includes("Goodbye")) {
  arr.reverse();
} else if (arr.includes("Cruel")) {
  arr.reverse();
}
console.log(arr); // ["Hello", "5", "4", "World", "Cruel", "Goodbye", "World", "Hello"] - Shows that the original array was modified


// sort() - Sorts the elements of an array in place and returns the array. The default sort order is built upon converting each element into a string, then comparing their sequences of UTF-16 code units values.
arr.sort(); // Sorts the elements of the array in place and returns the array
            // If no compare function is provided, the array elements are converted to strings and then sorted as strings.
            // The sort is not necessarily stable: elements that compare equal do not necessarily remain in their original order.
console.log(arr); // ["Hello", "Hello", "5", "4", "Cruel", "Goodbye", "World", "World"] - Shows that the original array was modified

// filter() - Creates a new array with all elements that pass the test implemented by the provided function.
var filteredArr = arr.filter((value) => value.length > 4);
console.log(filteredArr); // ["Hello", "Hello", "Cruel", "Goodbye", "World", "World"] - Shows that the original array was not modified

// map() - Creates a new array populated with the results of calling a provided function on every element in the calling array.
console.log(filteredArr); // ["Hello", "Hello", "Cruel", "Goodbye", "World", "World"] - Shows that the original array was not modified

var mappedArr = filteredArr.map((value) => value.length);
console.log(mappedArr); // [5, 5, 5, 7, 5, 5] - Shows that the original array was not modified

// forEach() - Calls a function for each element in the array.
var sum = 0;
filteredArr.forEach((num) => sum += num.length);
console.log(sum); // 17 - Shows that the original array was not modified and the sum of the lengths of the elements in the filtered array

// every() - Tests whether all elements in the array pass the test implemented by the provided function.
var allLongerThanFour = filteredArr.every((value) => value.length > 4);
console.log(allLongerThanFour); // true - Shows that all elements in the filtered array have a length greater than 4

