// Scripts used to manage the UI functionality for the programming challenge editor screen.

const code_tester = require("./test-code.js");
var CodeMirror = require("codemirror");
require("codemirror/mode/python/python.js");

// Set up code mirror editor
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

/**
 * Retrieves code from the code mirror editor, runs all the test cases then updates the results table.
 * Disables the "CHECK" button and shows a loading spinner while request is being processed.
 */
function sendCodeToJobe() {
  // Replaces all user input parameters to be blank so it matches the expected output
  // Takes into consideration cases input("thing)"), input('thing)'), input(thing) and int(input(thing))
  let code = myCodeMirror.getValue().replace(/(input\("[^"]+"\)|input\('[^']+'\)|input\([^)]+\))/mg, 'input()');

  $("#editor_run_button").prop("disabled", true);
  $(".code_running_spinner").css("display", "inline-block");

  code_tester.run_all_testcases(code, test_cases).then(result => {
    updateResultsTable(result);
    $("#editor_run_button").prop("disabled", false);
    $(".code_running_spinner").css("display", "none");
  });
}

/**
 * Updates the results table given some test case results.
 * @param {Array} results An array of test case results.
 */
function updateResultsTable(results) {
  for (result of results) {
    // Update status cell
    $(`#test-case-${result.id}-status`).text(result.status);

    // Update help modal
    $(`#test-case-${result.id}-help-title`).text(result.status)
    $(`#test-case-${result.id}-help`).text(result.helpInfo);
    $(`#test-case-${result.id}-help-icon`).show()

    // Update output cell
    $(`#test-case-${result.id}-output`).text(result.userOutput);

    // Update row colors
    var row_element = $(`#test-case-${result.id}-row`);
    if (result.status == "Passed") {
      row_element.addClass("table-success");
      row_element.removeClass("table-danger");
      row_element.removeClass("table-warning");
      $(`#test-case-${result.id}-help-icon`).hide()
      
    } else if (result.status == "Syntax Error") {
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

/**
 * Downloads text to a file.
 * @param {String} filename The filename of the file to be downloaded. 
 * @param {String} text The text content of the file to be downloaded.
 */
function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

/**
 * Downloads the editor code to a file called <current_challenge_slug>.py.
 */
function downloadCode() {
  download(current_challenge_slug + ".py", myCodeMirror.getValue());
}

// Setting up event listener for the check button to run the code.
let submitButton = document.getElementById("editor_run_button");
submitButton.addEventListener("click", sendCodeToJobe);

// Setting up event listener for the download button.
let downloadButton = document.getElementById("download_button");
downloadButton.addEventListener("click", downloadCode);
