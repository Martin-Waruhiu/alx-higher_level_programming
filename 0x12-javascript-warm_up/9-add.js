#!/usr/bin/env node

function add (a, b) {
  const num1 = parseInt(a, 10); // Convert first argument to an integer
  const num2 = parseInt(b, 10); // Convert second argument to an integer

  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(num1 + num2); // Print the sum of the two numbers
  } else {
    console.log('Invalid numbers');
  }
}
// Get the command line arguments (excluding the first two default arguments)
const args = process.argv.slice(2);
add(args[0], args[1]);
