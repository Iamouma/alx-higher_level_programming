$.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        // Extracts the translation of "hello" from the fetched data
        const translation = data.hello;

        // Display the translation in the <div> with Id "hello"
        $('DIV#hello').text(translation);
      }
});
