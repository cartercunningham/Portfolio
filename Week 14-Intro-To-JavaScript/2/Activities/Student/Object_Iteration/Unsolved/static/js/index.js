// Array of recipe objects
var recipes = [
  { dish: "Fried fish", spice: "Dorrigo" },
  { dish: "Crab Rangoon", spice: "Akudjura" },
  { dish: "Pickled Okra", spice: "Chili pepper" },
  { dish: "Macaroni salad", spice: "Pepper" },
  { dish: "Apple butter", spice: "Avens" },
  { dish: "Pepperoni Pizza", spice: "Asafoetida" },
  { dish: "Hog fry", spice: "Peppermint" },
  { dish: "Corn chowder", spice: "Akudjura" },
  { dish: "Home fries", spice: "Celery leaf" },
  { dish: "Hot chicken", spice: "Boldo" }];

console.log(recipes);

// @TODO: YOUR CODE HERE

// # Recipes Objects


// In this activity, you will practice iterating over arrays of objects.

// ## Instructions

// * Create two empty arrays called `dishes` and `spices`.

var dishes=[];
var spices=[];

// // // * Use `Object.entries` and `forEach()` to iterate over an array of recipe objects.

recipes.forEach((recipe)=>console.log(recipe));

// // // Get the entries for each object in the array

Object.entries(recipes).forEach(([dish, spice]) => {
  if (dish==="dish"){
  dishes.push(value)
  }

if (spice="spice")

// // * Push each dish into the `dishes` array.

// // * Push each spice into the `spices` array.

// * Log each final array to the console.

// ## Bonus

// * Create both arrays using `map` instead of `forEach`.
