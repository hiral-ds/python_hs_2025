let name = "Hiral Shewale";
let age = "17";
let course = "Computer Technology";
let college = "K.K.Wagh Polytechnic";

let card = document.createElement('div');
card.style.width = '300px';
card.style.border = '2px solid black';
card.style.fontFamily = 'Arial';
// card.style.backgroundColor = 'pink';
card.style.textAlign = 'center';

let title = document.createElement('h2');
title.innerText = "Identity Card";

let nameLine = document.createElement('p');
nameLine.innerText = "Name: " + name;

let ageLine = document.createElement('p');
ageLine.innerText = "Age: " + age;

let courseLine = document.createElement('p');
courseLine.innerText = "Course: " + course;

let collegeLine = document.createElement('p');
collegeLine.innerText = "College: " + college;

card.appendChild(title);
card.appendChild(nameLine);
card.appendChild(ageLine);
card.appendChild(courseLine);
card.appendChild(collegeLine);

// Show the card on the page
document.body.appendChild(card);