// little practice with click Event:

const allButtons = document.querySelectorAll(".my-buttons button");
console.log(allButtons);

const body = document.querySelector("body");
console.log(body);

allButtons.forEach((button)=>{

    button.addEventListener("click",(e)=>{
        e.target.style.backgroundColor='pink';
        e.target.style.color='gray';
        console.log(e);
        console.log(e.target)
    })
})

const inputBox = document.getElementById("first-name")
console.log(inputBox);
inputBox.addEventListener("keyup",(e)=> {
    console.log(e);
    console.log(e.target);
})

/*

allButtons.forEach((button)=>{

    button.addEventListener("click",(e)=>{
        body.style.backgroundColor = 'yellow';
        button.style.backgroundColor = 'gray';
    })
})

*/