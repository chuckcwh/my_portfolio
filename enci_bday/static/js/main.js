$(document).ready(function(){

//    flip cards
    function toggleCard(slideName) {
        $('.bday_card').removeClass('show');
        $('.'+slideName).addClass('show');
    }

//    button - right/ wrong/ restart
    $('.btn').on('click', function() {
        var choose = $(this);
        var slideNumber = parseInt(choose.parent().parent().attr('class').split(' ')[1].split('e')[1]);
        slideNumber++;
        if (choose.hasClass('rightOne')) {
            slideName = "slide" + slideNumber + "_right"
            toggleCard(slideName);
        } else if (choose.hasClass('wrongOne')) {
            slideName = "slide" + slideNumber + "_wrong"
            toggleCard(slideName);
        } else if (choose.hasClass('restart')) {
            toggleCard("slide1");
        }

    });

});