$(document).ready(function(){

    $('#email_submit').on('click', function() {
        console.log("email send");
        var email_content = {
            name: $('#form-name').val(),
            email: $('#form-email').val(),
            number: $('#form-contact-number').val(),
            message: $('#message').val()
        };
        $('#email_submit_message').html('');
        console.log(email_content);
        $.ajax ({
            url: "/email_send/",
            type: "POST",
            dataType: "json",
            data: JSON.stringify(email_content),
            success: function(data) {
                console.log(data);
                $('#email_submit_message').html('<div class="alert">' + data + '</div>');
            }
        })
    })
});