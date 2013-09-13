// jQuery code
$('div.blue, span.red').addClass('bold').fadeIn(500);

// basically equivalent pure javascript code
var tags = ['div', 'span'];
var classes = ['blue', 'red'];
var all_sel_elements = [];
for (var i=0; i<tags.length; i++) {
    var elements = document.getElementsByTagName(tags[i]);
    for(var j=0; j<elements.length; j++) {
        var element = elements[j];
        if ((' ' + element.className + ' ').indexOf(' ' +
            classes[i] + ' ') > -1) {
            all_sel_elements.push(element);
            element.className += ' bold';
        }
}

var n=0;
var steps=100;
var duration = 500.;
var fader = function(){
    for (var i=0; i<all_sel_elements.length; i++) {
        all_sel_elements[i].style.opacity += 1./steps;
    }
    if (n++<steps){
        window.setTimeout(fader, duration/steps);
    }
}
window.setTimeout(fader, duration/steps);

