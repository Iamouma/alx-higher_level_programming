// Ensures the DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    // Selects the <header> element
    const headerElement = document.querySelector('header');

    // Checks if the element is present
    if (headerElement) {
        // Sets the text color to red
        headerElement.style.color = '#FF0000';
    } else {
        console.error('Header element not found.');
    }
});
