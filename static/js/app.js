// from data.js
var tableData = data;

// YOUR CODE HERE! - this is from the everyone file in day file
// Get a reference to the table body
var tbody = d3.select("tbody");

// Build table
data.forEach((sightingReport) => {
  var row = tbody.append("tr");
  Object.entries(sightingReport).forEach(([key, value]) => {
    var cell = tbody.append("td");
    cell.text(value);
  });
});


// Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();



  // Wipe current data in table
  tbody.selectAll("td").remove()

// Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var filteredData = data.filter(data => data.datetime === inputValue);

  console.log(filteredData);

  filteredData.forEach((sightingReport) => {
    var row = tbody.append("tr");
    Object.entries(sightingReport).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
  // var filteredData = people.filter(person => person.bloodType === inputValue);

  // console.log(filteredData);

});