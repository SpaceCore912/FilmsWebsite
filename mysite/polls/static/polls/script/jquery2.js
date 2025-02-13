let film = JSON.parse(document.getElementById('film').textContent)
$(document).ready(function() {
    $("#likeButton").click(function(event){
        event.preventDefault(); // Prevent the default button behavior
        
        
        //let likes =JSON.parse(document.getElementById("likes").textContent)
        $.ajax({
            type: "POST",
            url: "2",// The URL to send the request to
            data: {
                'film_id': film, // Send the film ID to the server
                'csrfmiddlewaretoken': '{{ csrf_token }}' // Ensure the CSRF token is sent
            },
            success: function(response) {
                // Handle a successful response
                if (response.liked) {
                    
                    $("#likeButton").addClass('clicked');
                    $("#likeButton .text").text('Liked' );
                    
                } else {
                    
                    $("#likeButton").removeClass('clicked');
                    $("#likeButton .text").text('Like');
                }
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error("An error occurred: " + error);
            }
        });
    });
});

$(document).ready(function(){
    $("#watchlist").click(function(event){
        event.preventDefault();
        let addedW=JSON.parse(document.getElementById('addedW').textContent)

$.ajax({
    type: "POST",
    url: "3",// The URL to send the request to
    data: {
        'film_id': film, // Send the film ID to the server
        'csrfmiddlewaretoken': '{{ csrf_token }}' // Ensure the CSRF token is sent
    },
    success: function(response) {
        // Handle a successful response
        if (response.added) {
            
            $("#watchlist").addClass('clicked');
            $("#watchlist .text").text('Added to watchlist');
            
        } else {
            
            $("#watchlist").removeClass('clicked');
            $("#watchlist .text").text('Add to watchlist');
        }
    },
    error: function(xhr, status, error) {
        // Handle errors
        console.error("An error occurred: " + error);
    }
});
});
});

