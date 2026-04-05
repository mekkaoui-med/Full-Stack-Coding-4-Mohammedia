let sentence = "the trip was not that bad";

let words = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (words !== -1 && wordBad !== -1 && wordBad > words) {
  let newSentence =
    sentence.slice(0, words) + "good" + sentence.slice(wordBad + 3);
  console.log(newSentence);
} else {
    console.log(sentence);
}
// console.log("The index of 'not' is : " + words);
// console.log("The index of 'bad' is : " + wordBad);

//If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”,
//  then console.log the result.For example, the result here should be : “The movie is good, I like it”
