$(document).ready(function () {
    // adds a click event to the translate button
    $('#btn_translate').click(function () {

        //gets language code entered by the user
        const languageCode = $('#language_code').val();

        // uses AJAX to fetch data
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
            method: 'GET',
            dataType: 'json',
            success: function (data) {
                // extracts translaton of hello from fetched data
                $('#hello').text(translation);
            },
            error: function () {
            // Handles any errors here
            $('#hello').text('Translation not found.');
            }
        });
    });
});
