console.log("something1");

var movies = [];

function getCatalog(){
    $.ajax({
        url: 'http://127.0.0.1:8000/rentals/movies',
        type: "GET",
        success: function(response){
            console.log("response from server", response);

            movies = response.objects;
            for(var i=0; i<movies.length; i++){
                displayMovie(movie[i]);
            }
        },
        error: function(errorDetails){
            console.log("Error", errorDetails);
        }
    });
}

function displayMovie(movie){
    var container = $("#container");

    var syntax =
    `<div>
        <img src = "${movie.image_url}">
        <h2>${movie.title}</h2>
    </div>
    `;

    container.append(syntax);
}

function init(){
    console.log("Catalog.js loaded");

    getCatalog();
}

window.onload = init;