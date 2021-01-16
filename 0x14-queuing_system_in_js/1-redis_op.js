const redis = require("redis");
const client = redis.createClient();

client.on("connect", () => {
  console.log(`Redis client connected to the server`);
});

client.on("error", () => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
  client.get(schoolName, redis.print);
}

function displaySchoolValue(schoolName) {
  console.log(schoolName);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
