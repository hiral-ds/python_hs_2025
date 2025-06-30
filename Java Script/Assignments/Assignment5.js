const button = document.getElementById("clickBtn");
const counterSpan = document.getElementById("counter");
let count = 0;

// First listener: count clicks
button.addEventListener("click", function () {
  count++;
  counterSpan.textContent = count;
});

// Second listener: log event details
button.addEventListener("click", function (event) {
  console.log("Event Type:", event.type);
  console.log("Time Stamp:", event.timeStamp);
  console.log("This Tag:", this.tagName);
});