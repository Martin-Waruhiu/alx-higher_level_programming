#!/usr/bin/node
// arguments count

const argz = process.argv.slice(2);

if (argz.length === 0) {
  console.log('No argument');
} else if (argz.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
