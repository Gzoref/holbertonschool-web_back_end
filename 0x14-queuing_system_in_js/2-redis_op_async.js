const redis = require("redis");
const client = redis.createClient();
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client);

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

async function displaySchoolValue(schoolName) {
  const result = await getAsync(schoolName);
  console.log(result);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
