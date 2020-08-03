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

// Set the editor to show the saved attempt if it exists
myCodeMirror.getDoc().setValue(saved_attempts[current_challenge_slug] ? saved_attempts[current_challenge_slug] : "");

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

  // Saved the users code
  let raw_code = myCodeMirror.getValue();
  save_code(raw_code)

  // Run the test_cases
  code_tester.run_all_testcases(code, test_cases).then(result => {
    updateResultsTable(result);
    $("#editor_run_button").prop("disabled", false);
    $(".code_running_spinner").css("display", "none");
  });
}

/**
 * Creates a request to save the users code in a django session.
 * @param {String} raw_code The users raw code attempt
 */
async function save_code(raw_code) {
  // Sets the saved attempt
  let data = {
      "challenge": current_challenge_slug,
      "attempt": raw_code
  }

  // Saves the code in the django session
  fetch(save_attempt_url, {
    method: "POST",
    headers: {
      "Content-type": "application/json; charset=utf-8",
      Accept: "application/json",
      "X-CSRFToken": csrf_token
    },
    body: JSON.stringify(data)
  });
}

/**
 * Updates the results table given some test case results.
 * @param {Array} results An array of test case results.
 */
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
