function filterFilms(category) {
    var films = document.querySelectorAll('.film');
    
    films.forEach(function(film) {
        if (category === 'all' ||  film.getAttribute('data-category').includes(category)) {
            film.style.display = 'block';
        } else {
            film.style.display = 'none';
        }
    });
}

