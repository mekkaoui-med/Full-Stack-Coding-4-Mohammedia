// 🌟 Exercise 1 : List of people :

console.log("-Partie I - Loops : ");

const people = ["Greg", "Mary", "Devon", "James"];
// Part I - Review about arrays :

// Write code to remove “Greg” from the people array.
console.log("**** EX-1****");
people.shift();
console.log(people);
console.log("**** EX-2****");

// Write code to replace “James” to “Jason”.
people.splice(2, 1, "Jason");
console.log(people);
//code to add my name to the end of the people array.
console.log("**** EX-3****");
people.push("Mohamed");
console.log(people);
// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
console.log("**** EX-4****");
let Mary_index = people.indexOf("Mary");
console.log("Mary's index is : " + Mary_index);
console.log("**** EX-5****");
// Write code to make a copy of the people array using the slice method. The copy should NOT include “Mary” or your name.
let people_copy = people.slice(1, 4);
console.log(people_copy);
// Write code that gives the index of “Foo”. Why does it return -1 ?
console.log("**** EX-5****");
let foo_index = people.indexOf("Foo");
console.log("Foo's index is : " + foo_index);
// It returns -1 because "Foo" is not in the array, and indexOf returns -1 when the element is not found.
console.log("**** EX-7****");
let last = people[people.length - 1];
console.log("The last element of the people array is : " + last);

// Part II - Loops :
console.log("**** EX-1****");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") {
    console.log("Found Devon at index " + i);
    break;
  }
}

console.log("-Partie II - Loops : ");

// 🌟 Exercise 2 : Your favorite colors :

// Create an array called colors where the value is a list of your five favorite colors.
console.log("**** EX-1****");
let colors = ["Blue", "Green", "Red", "Yellow", "Purple"];
let suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
  console.log("My " + (i + 1) + suffixes[i] + " choice is " + colors[i]);
}
// 🌟 Exercise 3 : Repeat the question :
const prompt = require("prompt-sync")();
let number;
do {
  number = parseInt(prompt("Please enter a number greater than 10: "));
} while (isNaN(number) || number <= 10);
//🌟 Exercise 4 : Building Management:
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};
// Console.log the number of floors in the building.
let NumberOfFloors = building.numberOfFloors;
console.log("The number of floors in the building is : " + NumberOfFloors);
// how many apartments are on the floors 1 and 3.
let apt_floor1 = building.numberOfAptByFloor.firstFloor;
let apt_floor3 = building.numberOfAptByFloor.thirdFloor;
console.log("The number of apartments on the first floor is : " + apt_floor1);
console.log("The number of apartments on the third floor is : " + apt_floor3);
//Console.log the name of the second tenant and the number of rooms he has in his apartment.
let second_tenant = building.nameOfTenants[1];
let rooms_dan = building.numberOfRoomsAndRent.dan[0];
console.log("The name of the second tenant is : " + second_tenant);
console.log("The number of rooms Dan has in his apartment is : " + rooms_dan);
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, then increase Dan’s rent to 1200.
let sarah_rent = building.numberOfRoomsAndRent.sarah[1];
let david_rent = building.numberOfRoomsAndRent.david[1];
let dan_rent = building.numberOfRoomsAndRent.dan[1];
console.log("Dan's last rent is : " + building.numberOfRoomsAndRent.dan[1]);

if (sarah_rent + david_rent > dan_rent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
  console.log("Dan's rent has been increased to 1200.");
}
console.log("Dan's current rent is : " + building.numberOfRoomsAndRent.dan[1]);
//🌟 Exercise 5 : Family :

// Create an object called family with a few key value pairs.
console.log("**** EX-1****");

let family = {
  father: "rachid",
  mother: "fatiha",
  son: "mohamed",
  daughter: "sara",
  familyname: "boudiaf",
  adress: "Algeria",
};
// Console.log the keys of the object.
console.log("The keys of the object are : ");
for (let x in family) {
  console.log(x);
}
// Console.log the values of the object.
// the values of the object are : rachid, fatiha, mohamed, sara, boudiaf, Algeria
console.log("The values of the object are : ");
for (let x in family) {
  console.log(family[x]);
}
//🌟 Exercise 6 : Rudolf :

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}
// Given the object above and using a for loop, console.log “my name is Rudolf the reindeer”
let sentence = "";
for (let key in details) {
    sentence += key + " " + details[key] + " ";
}
console.log(sentence.trim());
// Exercise 7 : Secret Group : 
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();``
let list = ""
for (let i = 0 ; i < names.length; i++) {
    list += names[i][0]
}
console.log("the company name is: " + list)


