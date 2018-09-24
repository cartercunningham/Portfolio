// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the weather data from data.js
console.log(data);

// Step 1: Loop Through `data` and console.log each weather report object

data.forEach((item,index) => {console.log(item)
});


// Step 2:  Use d3 to append one table row `tr` for each weather report object
// Don't worry about adding cells or text yet, just try appending the `tr` elements.

data.map((weatherData,index)=>{
    console.log(weatherData);
    console.log(weatherData.weekday);
    d3.select("tbody").append("tr").
                        append("td").text(weatherData.weekday)
                        .append("td").text(weatherData.date)
                        .append("td").text(weatherData.high)
                        .append("td").text(weatherData.low)
});

// Step 3:  Use `Object.entries` to console.log each weather report value



// Step 4: Use d3 to append 1 cell per weather report value (weekday, date, high, low)



// Step 5: Use d3 to update each cell's text with
// weather report values (weekday, date, high, low)



// BONUS: Refactor to use Arrow Functions!
