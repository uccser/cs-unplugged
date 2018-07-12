    var editor = CodeMirror(document.getElementById("codeeditor"), {
      lineNumbers : true,
      gutter: true,
      lineWrapping: true,
      autoRefresh: true,
      mode: "python"
    });

    var outputBox = CodeMirror(document.getElementById("outputBox"), {
      gutter: true,
      lineWrapping: true,
      readOnly: false,
      cursorBlinkRate: -1,
      mode: "python"
    });