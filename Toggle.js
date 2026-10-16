// Select the DOM elements
const toggleBtn = document.getElementById('dark-mode-btn');
const body = document.body;

//Atach event listener to intercept click
toggleBtn.addEventListener ('click', function() {
 body.classList.toggle('dark-theme');
});