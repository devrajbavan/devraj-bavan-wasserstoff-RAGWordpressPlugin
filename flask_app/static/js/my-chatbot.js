jQuery(document).ready(function($) {
    $('#chatbot-form').submit(function(event) {
        event.preventDefault();
        var question = $('#chatbot-question').val();
        $.ajax({
            url: '/get_answer',
            type: 'POST',
            data: {
                question: question
            },
            success: function(response) {
                $('#chatbot-answer').text(response.answer);
            },
            error: function(xhr, status, error) {
                $('#chatbot-answer').text('Error: ' + error);
            }
        });
    });
});
