const app = require('http');

app.createServer((request, result) => {
  result.write('Hello Holberton School!');
  result.end();
}).listen(1245);
