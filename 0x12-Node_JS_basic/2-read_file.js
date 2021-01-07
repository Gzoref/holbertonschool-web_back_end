const fs = require("fs");
const readline = require('readline');

function countStudents(database) {
  try {
    const readLine = fs.readFileSync(database, 'utf8');
    const lines = readLine.split(/\r?\n/);
    process.stdout.write(`Number of students: ${readLine}`)
  } catch (error) {
    throw new Error("Cannot load the database");
  }
};

module.exports = countStudents;