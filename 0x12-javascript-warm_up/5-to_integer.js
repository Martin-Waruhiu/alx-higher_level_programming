#!/usr/bin/node

const args = process.argv.slice(2); // Get the arguments passed to the script
const num = parseInt(args[0], 10); // Convert the first argument to an integer

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
