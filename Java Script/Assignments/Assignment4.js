// Way 1: Inline onclick (written directly in HTML)
function inlineClick(btn) {
  console.log("Way 1 clicked");
  changeBackground(btn);
}

// Way 2: element.onclick
const way2 = document.getElementById("way2");
way2.onclick = function () {
  console.log("Way 2 clicked");
  changeBackground(this);
};

// Way 3: addEventListener
const way3 = document.getElementById("way3");
way3.addEventListener("click", function () {
  console.log("Way 3 clicked");
  changeBackground(this);
});

// Reusable function to change bg color and revert
function changeBackground(btn) {
  const original = btn.style.backgroundColor;
  btn.style.backgroundColor = "green";
  setTimeout(() => {
    btn.style.backgroundColor = original;
  }, 500);
}