//js
const counter = document.getElementById("counter-number");

const url = "https://lfh7qeixuf.execute-api.us-east-1.amazonaws.com/Prod/hello";

async function updateCounter() {
  let response = await fetch(url);
  let data = await response.json();
  counter.innerHTML = ` Views: ${data.views}`;
}

updateCounter();
