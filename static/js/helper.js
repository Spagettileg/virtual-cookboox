// Flexible Textarea 

function makeExpandingArea(container) {
 var area = container.querySelector('textarea');
 var span = container.querySelector('span');
 if (area.addEventListener) {
   area.addEventListener('input', function() {
     span.textContent = area.value;
   }, false);
   span.textContent = area.value;
 } else if (area.attachEvent) {
   // IE8 compatibility
   area.attachEvent('onpropertychange', function() {
     span.innerText = area.value;
   });
   span.innerText = area.value;
 }
 
// Enable extra CSS for Textarea
container.className += "active";
}var areas = document.querySelectorAll('.expandingArea');
var l = areas.length;while (l--) {
 makeExpandingArea(areas[l]);
}

$(document).ready(function () {

    // Website authors developer years appear in the footer
     
    $('#developer-years').text('2018 - ' + new Date().getFullYear());
    
});

// Scroll to top of page function

    $("a[href='#move-up']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 800);
        return false;
    });

    // If position of vertical scroll is above 600px, to top button will disappear.
    $(window).scroll(function () {
        if ($(this).scrollTop() > 575) {
            $('.move-top').fadeIn();
        } else {
            $('.move-top').fadeOut();
        }
    });
