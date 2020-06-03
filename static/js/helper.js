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



