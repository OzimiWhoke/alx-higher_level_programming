$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: function(data) {
      var movies = data.results;
      var list = $('#list_movies');
      
      $.each(movies, function(index, movie) {
        var title = $('<li>').text(movie.title);
        list.append(title);
      });
    },
    error: function() {
      $('#list_movies').text("Error fetching movies.");
    }
  });
});
