// Exercise 1 : Divisible by three :
console.log("**** EX-1****");
// Loop through the numbers 0 to 100. Console.log all the numbers that are divisible by 3.
let numbers = [123, 8409, 100053, 3333333333, 7];

let list = "";

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 3 === 0) {
    list += numbers[i] + " ";
    console.log(true);
  } else {
    console.log(false);
  }
}
console.log(list);
// Exercise 2 : Attendance :
console.log("**** EX-2****");
const prompt = require("prompt-sync")();
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina",
};

let studentInput = prompt("Please enter the name of the student : ");
if (studentInput.toLowerCase() in guestList) {
    console.log(`Hi! I'm ${studentInput}, and I'm from ${guestList[studentInput.toLowerCase()]}.`);
} else {
    console.log("Hi! I'm a guest.");
}
// Exercise 3 : Playing with numbers :
console.log("**** EX-3****");
//Console.log the sum of all the numbers in the age array.
let age = [20,5,12,43,98,55];
let sum = 0;
for (let i = 0 ; i < age.length; i++) {
    sum += age[i];
}
console.log("The sum of all the numbers in the age array is : " + sum);
//Console.log the highest age in the array
let max = age[0];
for (let i = 1; i < age.length; i++) {
    if (age[i]> max) {
        max = age[i];
    }
}
console.log("The highest age in the array is : " + max);