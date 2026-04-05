// Exercise 1 : Checking the BMI:
console.log("**** EX-1****");
// 1
let med = {
  FullName: "Med Mekkoui",
  Mass: 75,
  Height: 1.8,
  BMI: function () {
    return this.Mass / (this.Height * this.Height);
  },
};
let ghochaf = {
  // nake name
  FullName: "Ghochaf",
  Mass: 85,
  Height: 1.75,
  BMI: function () {
    return this.Mass / (this.Height * this.Height);
  },
};
function compareBMI() {
  if (med.BMI() > ghochaf.BMI()) {
    console.log(
      `${med.FullName} has a higher BMI of ${med.BMI().toFixed(2)} compared to ${ghochaf.FullName}'s BMI of ${ghochaf.BMI().toFixed(2)}.`,
    );
  } else if (med.BMI() < ghochaf.BMI()) {
    console.log(
      `${ghochaf.FullName} has a higher BMI of ${ghochaf.BMI().toFixed(2)} compared to ${med.FullName}'s BMI of ${med.BMI().toFixed(2)}.`,
    );
  } else {
    console.log(
      `${med.FullName} and ${ghochaf.FullName} have the same BMI of ${med.BMI().toFixed(2)}.`,
    );
  }
}
compareBMI();
// Exercise 2 : Grade Average :
console.log("**** EX-2****");

function CalculateAvg(gradesList) {
  let sum = 0;
  for (let i = 0; i < gradesList.length; i++) {
    sum += gradesList[i];
  }
  return sum / gradesList.length;
}
function findAvg(gradesList) {
  let avg = CalculateAvg(gradesList);

  console.log("Average:", avg);

  if (avg >= 65) {
    console.log("You passed ");
  } else {
    console.log("You failed ");
  }
}
let grades = [85, 90, 8, 2, 88];
findAvg(grades);

