let moon = document.getElementById('moon');
let stars = document.getElementById('stars');
let mountains_front = document.getElementById('mountains_front');
let mountains_behind = document.getElementById('mountains_behind');
let text = document.getElementById('text');
let btn = document.getElementById('btn');
var sec = document.getElementById('sec')

window.addEventListener('scroll', function(){
    let value = window.scrollY;
    moon.style.top = value * 0+'px';
    mountains_behind.style.top = value *0.5 + 'px';
    mountains_front.style.top = value * 0 + 'px';
    text.style.marginRight = value *1 +'px';
    text.style.marginTop = value *1 +'px';
    btn.style.marginTop = value *1.5 +'px';
    sec.style.left = value *0.5+'px';
})


// Add the fade-in class to the body when the DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('fade-in');
});