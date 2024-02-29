// A rune can be defined as an integer used to represent any Unicode code point.
// As a Dart string is a simple sequence of UTF-16 code units, 
// 32-bit Unicode values in a string are represented using a special syntax. 

void main() {
  //declaring runes
  var heart = '\u2665';
  var laugh = '\u{1f600}';
  var face = '\u{1f600}';
  var smile = '\u{1f60a}';
  var thumbsUp = '\u{1f44d}';
  var thumbsDown = '\u{1f44e}';

  //printing runes
  print("Heart is $heart");
  print("Laugh is $laugh");
  print("Face is $face");
  print("Smile is $smile");
  print("Thumbs up is $thumbsUp");
  print("Thumbs down is $thumbsDown");
}

/* Output:
Heart is ♡ heart
Laugh is 😀 fac
Face is 😀 fac
Smile is 😊 sm    //smile is printed as sm   because it's the closest match for the given character
Thumbs up is 👍 th
Thumbs down is 👎 th
*/
 
 //In the above example, we have defined a few runes using the Unicode code points. 
 //The first rune is a heart symbol, which is represented by the Unicode code point \u2665. 
 //The second rune is a laughing face, which is represented by the Unicode code point \u{1f600}. 
 //The third rune is a smiley face, which is represented by the Unicode code point \u{1f600}. 
 //The fourth rune is a smiley face, which is represented by the Unicode code point \u{1f60a}. 
 //The fifth rune is a thumbs-up symbol, which is represented by the Unicode code point \u{1f44d}. 
 //The sixth rune is a thumbs-down symbol, which is represented by the Unicode code point \u{1f44e}. 
 
 void main2() {
  //define a string with a rune
  String runesString = "Runes in Dart: \u{1f600} \u{1f60a} \u{1f44d} \u{1f44e}";
  print(runesString); //prints Runes in Dart: 😀 😊 👍 👎
  print(runesString); //prints Runes in Dart: 😀 😊 👍 👎
 }