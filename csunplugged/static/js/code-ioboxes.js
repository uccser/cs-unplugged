var editor = CodeMirror(document.getElementById("outputField"), {
  lineNumbers : true,
  gutter: true,
  lineWrapping: true,
  autoRefresh: true,
  mode: "python"
});

/*var outputBox = CodeMirror(document.getElementById("outputBox"), {
  gutter: true,
  lineWrapping: true,
  readOnly: false,
  cursorBlinkRate: -1,
  mode: "python"
});*/

window.onload = function(){
  $('.CodeMirror-scroll').addClass('editor-height');
  $('.CodeMirror').addClass('editor-height');
  $('.CodeMirror').addClass('infinite-stretch')
}