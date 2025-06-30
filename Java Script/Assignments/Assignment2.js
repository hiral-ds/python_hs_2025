const buttons = document.querySelectorAll("button");

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function () {
    console.log(`You clicked button ${i + 1}: ${this.textContent}`);
  });
}