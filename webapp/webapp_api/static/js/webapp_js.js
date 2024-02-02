function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}


$(document).ready(function () {
    $('#add, #subtract, #multiply, #divide').click(function () {
        var operation = $(this).attr('id');
        var numberA = parseFloat($('#numberA').val());
        var numberB = parseFloat($('#numberB').val());

        // Получаем CSRF-токен
        var csrftoken = getCookie('csrftoken');

        // Отправляем AJAX-запрос
        $.ajax({
            url: '/api_v1/' + operation + '/',
            type: 'POST',
            data: JSON.stringify({"A": numberA, "B": numberB}),
            contentType: 'application/json',
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (response) {
                $('#result').css('color', 'green').text("Answer: " + response.answer);
            },
            error: function (response) {
                $('#result').css('color', 'red').text("Error: " + response.responseJSON.error);
            }
        });
    });
});