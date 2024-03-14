var current_color = '';
var heights = document.querySelectorAll('tr');
var widths = heights[0].querySelectorAll('td');

for (var i = 0; i < heights.length; i++) {
    for (var j = 0; j < widths.length; j++) {
        widths[j].addEventListener('click', console.log('Clicked!', i, j));
    };
};