// Jquery script
$(document).ready(function () {
  // use the jquery selector
  const element = $('header');

  // check if header is present
  if (element) {
    // set color
    element.css('color', '#FF0000');
  } else {
    console.error('Header element not found');
  }
});
