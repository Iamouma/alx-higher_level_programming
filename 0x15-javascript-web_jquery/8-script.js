$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        // extracts character from the fetched data
        const movieTitles = data.results.map(function (movie) {
            return movie.title;
        })

        // get the <ul> elements
        const listElement = $('UL#list_movies');
        
        // loops throught & append
        $.each(movieTitles, function (index, title) {
            const listItem = $('<li>' + title + '</li>');
            listElement.append(listItem);
        })
    }
});
