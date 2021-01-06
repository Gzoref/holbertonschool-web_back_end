const app = require('http');

app.createServer((request, result) => {
  result.end('Hello Holberton School!');
}).listen(1245);

module.exports = app;
