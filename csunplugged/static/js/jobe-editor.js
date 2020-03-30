// Set up code mirror
let myTextarea = document.getElementById("codemirror_editor");
let myCodeMirror = CodeMirror.fromTextArea(myTextarea, {
  mode: {
    name: "python",
    version: 3,
    singleLineStringErrors: false
  },
  lineNumbers: true,
  textWrapping: false,
  styleActiveLine: true,
  autofocus: true,
  indentUnit: 4,
  viewportMargin: Infinity,
  // Replace tabs with 4 spaces. Taken from https://stackoverflow.com/questions/15183494/codemirror-tabs-to-spaces
  extraKeys: {
    Tab: function(cm) {
      cm.replaceSelection("    ", "end");
    }
  }
});

// Send code to jobe and get a result
function sendCodeToJobe() {
  let code = myCodeMirror.getValue();

  run_all_testcases(code, test_cases).then(result => {
    updateResultsTable(result);
  });
}

function updateResultsTable(results) {
  for (result of results) {
    // Update status cell
    let status_element = $("#test-case-" + result.id + "-status");
    status_element.text(result.status);

    // Update output cell
    var output_element = $("#test-case-" + result.id + "-output");
    output_element.text(result.userOutput);

    // Update row colors
    var row_element = $("#test-case-" + result.id + "-row");
    if (result.status == "Passed") {
      row_element.addClass("table-success");
      row_element.removeClass("table-danger");
      row_element.removeClass("table-warning");
    } else if (result.status == "Compiler Error") {
      row_element.addClass("table-warning");
      row_element.removeClass("table-danger");
      row_element.removeClass("table-success");
    } else {
      row_element.addClass("table-danger");
      row_element.removeClass("table-success");
      row_element.removeClass("table-warning");
    }
  }
}

let submitButton = document.getElementById("editor_run_button");
submitButton.addEventListener("click", sendCodeToJobe);
