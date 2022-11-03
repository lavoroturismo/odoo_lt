$(document).ready(function () {

    setInterval(function(){ 
        var qualifica = $('#o_field_input_748').val();
        var client    = $('#o_field_input_747').val();
        var name      = $('input[name="name"]').val();
        if ( qualifica && client ) {
            $('input[name="name"]').val( qualifica + '  - ' + client );
        } else {
            $('input[name="name"]').val( '' );
        }
    }, 1000);

    console.log( 'I\'m here' );

})
