// Scripts used to manage the UI functionality for the programming challenge editor screen.

const codeTester = require("./test-code.js");
const editorUtils = require("./editor-options-menu.js")

var CodeMirror = require("codemirror");
var Scramble = require("./scramble.js");
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
var saved_attempt = saved_attempts[current_challenge_slug];
if (saved_attempt) {
  try {
    myCodeMirror.getDoc().setValue(Scramble.decode(saved_attempt["code"], saved_attempt["encode_key"], saved_attempt["encode_ver"]));
  } catch (e) { // Fall back to displaying nothing
    console.warn(e);
    myCodeMirror.getDoc().setValue("");
  }
} else {
  myCodeMirror.getDoc().setValue("");
}

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

  // Run the test_cases
  codeTester.run_all_testcases(code, test_cases).then(result => {
    updateResultsTable(result);

    // Saving the users code
    save_code(allCorrect(result) ? "passed" : "failed")

    $("#editor_run_button").prop("disabled", false);
    $(".code_running_spinner").css("display", "none");
  });
}

/**
 * Returns if the user has passed all test cases.
 * @param {Array} results An array of the test case results 
 * @return {Array} If all the test cases passed returns "Passed", otherwise "Failed"
 */
function allCorrect(results) {
  for (result of results) {
    if (result.status != "Passed") {
      return false
    }
  }
  return true
}

/**
 * Creates a request to save the users code in a django session.
 * @param {String} status If the user has Started, Passed or Failed the challenge.
 */
async function save_code(status="started") {
  let raw_code = myCodeMirror.getValue();
  let scramble_key = Scramble.randomKey(6);
  let scrambled = Scramble.encode(raw_code, scramble_key);
  let scrambled_code = scrambled[0];
  let scramble_version = scrambled[1];

  // Sets the saved attempt
  let data = {
      "challenge": current_challenge_slug,
      "attempt": scrambled_code,
      "status": status,
      "encode_key": scramble_key,
      "encode_ver": scramble_version,
  }

  // Saves the code in the django session
  let response = await fetch(save_attempt_url, {
    method: "POST",
    headers: {
      "Content-type": "application/json; charset=utf-8",
      Accept: "application/json",
      "X-CSRFToken": csrf_token
    },
    body: JSON.stringify(data)
  });

  return response;
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
    $(`#test-case-${result.id}-help-icon`).css('visibility','visible');

    // Update output cell
    $(`#test-case-${result.id}-output`).text(result.userOutput);

    // Update row colors
    var row_element = $(`#test-case-${result.id}-row`);
    if (result.status == "Passed") {
      row_element.addClass("table-success");
      row_element.removeClass("table-danger");
      row_element.removeClass("table-warning");
      $(`#test-case-${result.id}-help-icon`).css('visibility','hidden');
      
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
$("#editor_run_button").click(sendCodeToJobe);

// Setting up event listener for the download button.
$("#download_button").click(downloadCode);

// Apply the navigation setup
editorUtils.setupLessonNav()

// Save code when the user navigates using the next or prev buttons or opening nav
// Manually navigating to the next page to ensure code is saved first before the page reloads.
$("#prev_challenge_button").on("click", () => save_code().then(() => window.location.href = editorUtils.getPreviousChallengeURL()));
$("#next_challenge_button").on("click", () => save_code().then(() => window.location.href = editorUtils.getNextChallengeURL()));
$("#lessons_nav_toggle").on("click", () => save_code());
