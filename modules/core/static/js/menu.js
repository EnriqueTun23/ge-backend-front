// $(document).ready(function(){
// 	var altura = $('#menu').offset().top;
//     $( window ).scroll(function() {
//         if ( $(window).scrollTop() === 0  ){
//             $('#menu').removeClass('menu-fixed');
//         } else {
//             $('#menu').addClass('menu-fixed');
//         }
//     });
// });

$(document).bind("click", function (event) {
    children = $('.submenu').children('.children').hasClass('children-effect-end')
    menu = $('.menu-responsive-data').hasClass('menu-responsive-effect-end')
    if($(event.target).closest('.children, .submenu').length === 0) {
        if (children === true) {
            $('#hover-user').addClass('hover-plus').removeClass('user-menu-activate')
            $('.submenu').children('.children').addClass('children-effect-inicial').removeClass('children-effect-end')
        }
    }
})
$('.submenu').click(function(){
    $(this).children('.children').toggleClass('children-effect-inicial children-effect-end')
    if($('#hover-user').hasClass('hover-plus')) {
        $('#hover-user').addClass('user-menu-activate').removeClass('hover-plus')
        
    } else {
        $('#hover-user').addClass('hover-plus').removeClass('user-menu-activate')
        
    }
});

$('#logo-menu').click(function() {
    $('#menu-toogle').sidebar('toggle');
})

function EfectMenuHideShow() {
    if ($("#icon-hide-effect").hasClass('left')) {
        $('#icon-hide-effect').addClass('right').removeClass('left')
        $('.hidden-menu').css('position', 'relative').animate({
            left: '-70px',
        })
        $('.menu-vertical-class').animate ({
            width: '1%'
        })
        $('.container-data').animate ( {
            width: '98%' 
        })
        $('.icon-hidden').hide()
    }else {
        $('#icon-hide-effect').addClass('left').removeClass('right')
        
        $('.hidden-menu').css('position', 'relative').animate({
            left: '0px',
        })
        $('.menu-vertical-class').animate ({
            width: '6%'
        })
        $('.icon-hidden').show()
        $('.container-data').animate ( {
            width: '94%' 
        })
    }
}
function HideMenu() {
    if($('.icons-effects').hasClass('up')) {
        $('.icons-effects').addClass('down').removeClass('up')
        // $('.eliminar').slideUp();
        $('.eliminar').hide()
        $('.icons-effects-data').text('Más')
        $('.btn-admi').animate({
            height: '5%'
        })
        $('.btn-rol').animate({
            height: '80%'
        })
        $('.btn-admi').children('ul').children('li').animate({
            height: '100%'
        })
        // $('.menu-responsive-data').animate({
        //     height: '360px'
        // }, 150);
    } else {
        $('.icons-effects').addClass('up').removeClass('down')
        // $('.eliminar').slideDown();
        $('.eliminar').show()
        $('.icons-effects-data').text('Menos')
        // $('.menu-responsive-data').animate({
        //     height: '449px'
        // }, 50);
        $('.btn-admi').animate({
            height: '30%'
        })
        $('.btn-admi').children('ul').children('li').animate({
            height: '25%'
        })
        $('.btn-rol').animate({
            height: '62%'
        })
    }
}