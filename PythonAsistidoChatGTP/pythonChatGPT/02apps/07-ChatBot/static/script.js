$(document).ready(function(){
    $('#chat-form').on('submit', function(event){
        event.preventDefault();
        var user_input = $('#prompt').val();
        $.ajax({
            url: '/chat',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({prompt: user_input}),
            success: function(response){
                $('#response').html('<p>' + response.response + '</p>');
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});
