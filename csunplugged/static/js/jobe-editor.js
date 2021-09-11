// Scripts used to manage the UI functionality for the programming challenge editor screen.

const codeTester = require("./test-code.js");
const editorUtils = require("./editor-options-menu.js");
const utils = require("./utils.js");

// Python editor imports
var CodeMirror = require("codemirror");
require("codemirror/mode/python/python.js");

// Blockly editor imports
const Blockly = require('blockly');
const setupBlockly = require("./custom-blockly-blocks.js");
require('blockly/python');


// Has to be global as other functions are using these variables
var myCodeMirror; 
var workspace;
// Set up code mirror or blockly editor depending what programming_lang is from URL (/python or /block-based)
if (programming_lang == "python") {
  let myTextarea = document.getElementById("codemirror_editor");
  myCodeMirror = CodeMirror.fromTextArea(myTextarea, {
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

} else {
  // Set up blockly editor
  document.addEventListener("DOMContentLoaded", function () {

    // Set the math_change block to contain the values_number block by default.
    Blockly.Variables.flyoutCategoryBlocks = function(workspace) {
      var variableModelList = workspace.getVariablesOfType('');
    
      var xmlList = [];
      if (variableModelList.length > 0) {
        // New variables are added to the end of the variableModelList.
        var mostRecentVariable = variableModelList[variableModelList.length - 1];
        if (Blockly.Blocks['variables_set']) {
          var block = Blockly.utils.xml.createElement('block');
          block.setAttribute('type', 'variables_set');
          block.setAttribute('gap', Blockly.Blocks['math_change'] ? 8 : 24);
          block.appendChild(
              Blockly.Variables.generateVariableFieldDom(mostRecentVariable));
          xmlList.push(block);
        }
        if (Blockly.Blocks['math_change']) {
          var block = Blockly.utils.xml.createElement('block');
          block.setAttribute('type', 'math_change');
          block.setAttribute('gap', Blockly.Blocks['variables_get'] ? 20 : 8);
          block.appendChild(
              Blockly.Variables.generateVariableFieldDom(mostRecentVariable));
          var value = Blockly.Xml.textToDom(
              '<value name="DELTA">' +
              '<block type="values_number">' +
              '<field name="NUM">1</field>' +
              '</block>' +
              '</value>');
          block.appendChild(value);
          xmlList.push(block);
        }
    
        if (Blockly.Blocks['variables_get']) {
          variableModelList.sort(Blockly.VariableModel.compareByName);
          for (var i = 0, variable; (variable = variableModelList[i]); i++) {
            var block = Blockly.utils.xml.createElement('block');
            block.setAttribute('type', 'variables_get');
            block.setAttribute('gap', 8);
            block.appendChild(Blockly.Variables.generateVariableFieldDom(variable));
            xmlList.push(block);
          }
        }
      }
      return xmlList;
    };

    // Custom Blockly Theme
    var blocklyTheme = Blockly.Theme.defineTheme('block-based-scratch', {
      "base": Blockly.Theme.Classic,
      "blockStyles": {
        "values_blocks": {
          "colourPrimary": "#FF6680",
          "colourSecondary": "#FFABB9",
          "colourTertiary": "#FF4A68",
        },
        "looks_blocks": {
          "colourPrimary": "#9966FF",
          "colourSecondary": "#BB99FF",
          "colourTertiary": "#774DCB",
        },
        "control_blocks": {
          "colourPrimary": "#FFAB19",
          "colourSecondary": "#FFBE4D",
          "colourTertiary": "#CF8B17",
        },
        "sensing_blocks": {
          "colourPrimary": "#5CB1D6",
          "colourSecondary": "#87BED6",
          "colourTertiary": "#2E8EB8",
        },
        "operators_blocks": {
          "colourPrimary": "#59C059",
          "colourSecondary": "#7EBF7E",
          "colourTertiary": "#3D9438",
        },
        "variable_blocks": {
          "colourPrimary": "#FF8D1A",
          "colourSecondary": "#FFA64D",
          "colourTertiary": "#DB6E00",
        },
      },
      "categoryStyles": {
        "values_category": {
          "colour": "#FF6680",
        },
        "looks_category": {
          "colour": "#9966ff",
        },
        "control_category": {
          "colour": "#ffab19",
        },
        "sensing_category": {
          "colour": "#5cb1d6",
        },
        "operators_category": {
          "colour": "#59c059",
        },
        "variable_category": {
          "colour": "#ff8d1a",
        },
      },
      "componentStyles": {
        "toolboxBackgroundColour": "#f7f7f7",
        "flyoutBackgroundColour": "#e9ecef"
      }
    });

    // Add the custom Scratch-like Blockly blocks
    setupBlockly(Blockly);

    var toolbox = document.getElementById('toolbox');
    /* Workspace configurations */
    var options = {
      theme: blocklyTheme,
      renderer: 'zelos',
      toolbox : toolbox,
      collapse : true,
      comments : true,
      disable : true,
      maxBlocks : Infinity,
      trashcan : true,
      horizontalLayout : false,
      toolboxPosition : 'start',
      css : true,
      media : 'https://blockly-demo.appspot.com/static/media/',
      rtl : false,
      scrollbars : true,
      sounds : true,
      oneBasedIndex : true,
      zoom : {
        controls : true,
        wheel : true,
        startScale : 0.9,
        maxScale : 2,
        minScale : 0.5,
        scaleSpeed : 1.2
      }
    };
    /* Injects the blockly workspace */
    workspace = Blockly.inject('blocklyDiv', options);

    // Displays the user's previous block-based submission 
    if (previous_block_based_submission) {
      // Decodes the previous_block_based_submission which contains HTML entities. Outputs a string, and it converts it to XML
      var xml_node = Blockly.Xml.textToDom(utils.decodeHTMLEntities(previous_block_based_submission));

      Blockly.Xml.domToWorkspace(xml_node, workspace);
    }
  })
}

/**
 * Retrieves code from the code mirror editor, runs all the test cases then updates the results table.
 * Disables the "CHECK" button and shows a loading spinner while request is being processed.
 */
function sendCodeToJobe() {
  var code = '';
   if (programming_lang == 'python') {
     // Replaces all user input parameters to be blank so it matches the expected output
     // Takes into consideration cases input("thing)"), input('thing)'), input(thing) and int(input(thing))
     code = myCodeMirror.getValue().replace(/(input\("[^"]+"\)|input\('[^']+'\)|input\([^)]+\))/mg, 'input()');
   } else {
     // converts Blockly-code to Python
     const lang = 'Python';
     code = Blockly[lang].workspaceToCode(workspace);
   }

   console.log("SEND CODE TO JOBE")
   console.log(code)

  $("#editor_run_button").prop("disabled", true);
  $(".code_running_spinner").css("display", "inline-block");

  // Run the test_cases
  codeTester.run_all_testcases(code, test_cases).then(result => {
    updateResultsTable(result);

    // Saving the users code
    save_code(allCorrect(result) ? "passed" : "failed");

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
      return false;
    }
  }
  return true;
}

/**
 * Creates a request to save the users code in a django session.
 * @param {String} status If the user has Started, Passed or Failed the challenge.
 */
async function save_code(status="started") {
  var raw_code;
  if (programming_lang == "python") {
     raw_code = myCodeMirror.getValue();
  } else {
    xml_code = Blockly.Xml.workspaceToDom(Blockly.getMainWorkspace());
    raw_code = Blockly.Xml.domToText(xml_code);
  }
  // Sets the saved attempt
  let data = {
      "challenge": current_challenge_slug,
      "attempt": raw_code,
      "status": status,
      "programming_language": programming_lang
  };

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
    console.log(result)
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
  var code;
  if (programming_lang == "python") {
    code = myCodeMirror.getValue()
  } else {
    const lang = 'Python';
    code = Blockly[lang].workspaceToCode(workspace);
  }
  download(current_challenge_slug + ".py", code);
 }

/**
 * Retrieves the code from the blockly editor, converts it to JavaScript, runs the code.
 */
function runCode() { 
    // Convert blockly code to JavaScript
    const lang = 'JavaScript';
    const code = Blockly[lang].workspaceToCode(workspace);
 
    console.log(code);
 
    // Run JavaScript code
    try {
      eval(code);
    } catch (error) {
      console.log(error);
    }
  }

// Setting up event listener for the check button to run the code.
$("#editor_check_button").click(sendCodeToJobe);

// Setting up event listener for the download button.
$("#download_button").click(downloadCode);

// Setting up event listener for the run button to run the code
$("#blockly_editor_run_program_button").click(runCode);

// Apply the navigation setup
editorUtils.setupLessonNav();

// Save code when the user navigates using the next or prev buttons or opening nav
// Manually navigating to the next page to ensure code is saved first before the page reloads.
$("#prev_challenge_button").on("click", () => save_code().then(() => window.location.href = editorUtils.getPreviousChallengeURL()));
$("#next_challenge_button").on("click", () => save_code().then(() => window.location.href = editorUtils.getNextChallengeURL()));
$("#lessons_nav_toggle").on("click", () => save_code());
