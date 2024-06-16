    // Add the fade-in class to the body when the DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('fade-in');
    AOS.init();
});

document.addEventListener('DOMContentLoaded', function () {
    const text = document.querySelector('#text');
    const textContent = text.textContent;
    text.textContent = '';
    let index = 0;

    function typeEffect() {
        if (index < textContent.length) {
            text.textContent += textContent.charAt(index);
            index++;
            setTimeout(typeEffect, 100); // Adjust typing speed here
        }
    }

    typeEffect();
});
