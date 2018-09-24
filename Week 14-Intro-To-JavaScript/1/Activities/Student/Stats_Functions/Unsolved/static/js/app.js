var movieScore = [4.4, 3.3, 5.9, 8.8, 1.2, 5.2, 7.4, 7.5, 7.2, 9.7, 4.2, 6.9];

function mean(movieScore) {
// Starting a rating count
var sum = 0;

// Use a for loop to iterate through the movie scores
for (var i = 0; i < movieScores.length; i++) {

  // Add each score to the ratings count
  var score = movieScores[i];
  sum += score;
}
// Find the average score
var avg = sum / movieScores.length;

console.log(`The average is: ${avg}`)