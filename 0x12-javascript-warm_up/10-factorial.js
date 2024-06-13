#!/usr/bin/node

const arg = process.argv.slice(2);

const num = parseInt(arg[0], 10)

function factorial(n)
{
	if (n === 0) {
		return (1);
	}
	else{
		return(n * factorial(n-1));
	}
}
if (!isNaN(num)){
	console.log(`${factorial(num)}`);
}
else {
	return(1);
}
