// console.log("this js is working");

// const button = document.getElementById('personalButton');
// button.innerHTML = "Hover Me";
// button.addEventListener('mouseenter', func1);
// button.addEventListener('mouseleave', func2);


// function func1() {
//     button.style = "transition: 0.5s;";
//     button.innerText = "Personal detail";

// }

// function func2() {
//     button.style = "transition: 0.5s;";
//     button.innerText = "hover me";

// }

// button.forEach(btn => {
//     btn.addEventListener('click', function(e) {
//         let x = e.clientX - e.target.offsetLeft;
//         let y = e.clientY - e.target.offsetTop;
//         let ripple = document.createElement('span');
//         ripple.style.left = x + 'px';
//         ripple.style.top = y + 'px';
//         this.appendChild(ripple);

//     });
// }); 


// const buttons = document.getElementsByClassName('presonalButton');
const buttons = document.querySelectorAll('bro');



buttons.forEach(btn => {
    btn.addEventListener('click', function(e) {
        let x = e.clientX - e.target.offsetLeft;
        let y = e.clientY - e.target.offsetTop;
        console.log(x, y)
        let ripples = document.createElement('bros');
        ripples.style.left = x - (690) + 'px';
        ripples.style.top = y - 35 + 'px';
        console.log(ripples)
        this.appendChild(ripples);

        setTimeout(() => {
            ripples.remove()
        }, 1000);
    })


});