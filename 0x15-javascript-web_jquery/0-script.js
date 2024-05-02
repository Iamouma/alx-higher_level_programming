// select the element
const element = document.querySelector('header');

// check if element is present
if (element) {
    // set the color
    element.style.color = '#FF0000';
} else {
    console.error('Header element not found');
}
