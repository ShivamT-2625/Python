const client = require("./client")

async function init() {
  const result = await client.get("something:1")
  console.log("Result=>", result);
}

async function init__() {
  await client.expire("something:1", 10)  ## expires the client set data in 10 seconds
  // const set = await client.set("something:1", "TMKC")
  console.log("EHEE")
  
}
init();
init__()