#!/usr/bin/node

const arg = process.argv.slice(2);

const num = parseInt(arg[0], 10);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    let line = '';
    for (let j = 0; j < num; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
