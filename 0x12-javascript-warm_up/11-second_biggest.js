#!/usr/bin/node

const args = process.argv.slice(2);

// Check if there are no arguments or only one argument
if (args.length === 0 || args.length === 1) {
    console.log(0);
} else {
    // Convert arguments to integers
    const numbers = args.map(arg => parseInt(arg, 10));
    
    // Remove duplicates and sort the array in descending order
    const uniqueNumbers = [...new Set(numbers)].sort((a, b) => b - a);
    
    // Check if we have at least two distinct numbers
    if (uniqueNumbers.length < 2) {
        console.log(0);
    } else {
        // The second largest number is the second element in the sorted array
        console.log(uniqueNumbers[1]);
    }
}
