var id1 = document.getElementById('id1');

id1.onClick = function(evt){
  var id3 = document.getElementsByTagName('div')[0];
  id3.className += ' class2';
  id3.innerHTML = 'Don\'t leave yet!';
}