const readline = require('readline');
const { exec } = require('child_process');

const name = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

name.question('Welcome to Holberton School, what is your name?\n', (name) => {
  process.stdout.write(`Your name is: ${name}`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
