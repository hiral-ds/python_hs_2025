const buttons = document.querySelectorAll("button");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    console.log(this); // 'this' refers to window or undefined in strict mode
  });
});