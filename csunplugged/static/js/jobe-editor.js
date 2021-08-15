// Scripts used to manage the UI functionality for the programming challenge editor screen.

const codeTester = require("./test-code.js");
const editorUtils = require("./editor-options-menu.js")
const utils = require("./utils.js")

// Python editor imports
var CodeMirror = require("codemirror");
require("codemirror/mode/python/python.js");

// Blockly editor imports
const Blockly = require('blockly/core');
require('blockly/blocks');
require('blockly/python');
require('blockly/javascript');
const En = require('blockly/msg/en');
Blockly.setLocale(En);

// Has to be global as other functions are using these variables
let myCodeMirror; 
let workspace;
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
    // Custom Blockly blocks to look and act like Scratch
    Blockly.defineBlocksWithJsonArray([
      // Looks say block
      {
        "type": "looks_say",
        "message0": "say %1 %2",
        "args0": [
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "value"
          }
        ],
        "inputsInline": true,
        "previousStatement": null,
        "nextStatement": null,
        "colour": 240,
        "tooltip": "Say the specified text, number or other value.",
        "helpUrl": ""
      },
      // Operators modulo block
      {
        "type": "operators_modulo",
        "message0": "%1 mod %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "a",
            "check": "Number"
          },
          {
            "type": "input_dummy",
            "align": "CENTRE"
          },
          {
            "type": "input_value",
            "name": "n",
            "check": "Number"
          }
        ],
        "inputsInline": true,
        "output": "Number",
        "colour": '#7459c0',
        "tooltip": "Return the modulo of the two numbers.",
        "helpUrl": ""
      },
      // Operators multiply block
      {
        "type": "operators_multiply",
        "message0": "%1 * %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "x",
            "check": "Number"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "y",
            "check": "Number"
          }
        ],
        "inputsInline": true,
        "output": "Number",
        "colour": 120,
        "tooltip": "Return the product of the two numbers.",
        "helpUrl": ""
      },
      // Operators divide block 
      {
        "type": "operators_divide",
        "message0": "%1 / %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "x",
            "check": "Number"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "y",
            "check": "Number"
          }
        ],
        "inputsInline": true,
        "output": "Number",
        "colour": 120,
        "tooltip": "Return the quotient of the two numbers.",
        "helpUrl": ""
      },
      // Operators add block 
      {
        "type": "operators_add",
        "message0": "%1 + %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "x",
            "check": "Number"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "y",
            "check": "Number"
          }
        ],
        "inputsInline": true,
        "output": "Number",
        "colour": 120,
        "tooltip": "Return the sum of the two numbers.",
        "helpUrl": ""
      },
      // Operators subtract block
      {
        "type": "operators_subtract",
        "message0": "%1 - %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "x",
            "check": "Number"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "y",
            "check": "Number"
          }
        ],
        "inputsInline": true,
        "output": "Number",
        "colour": 120,
        "tooltip": "Return the difference of the two numbers.",
        "helpUrl": ""
      },
      // Operators join/concatenate string block
      {
        "type": "operators_join_string",
        "message0": "join %1 %2 %3",
        "args0": [
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "a",
            "check": "String"
          },
          {
            "type": "input_value",
            "name": "b",
            "check": "String"
          }
        ],
        "inputsInline": true,
        "output": "String",
        "colour": 120,
        "tooltip": "Returns a combination of the two input strings added together.",
        "helpUrl": ""
      },
      // Operators letter <num> of <string> block
      {
        "type": "operators_letter_of",
        "message0": "letter %1 %2 of %3 %4",
        "args0": [
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "index",
            "check": "Number"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "word",
            "check": "String"
          }
        ],
        "output": "String",
        "colour": 120,
        "tooltip": "Returns the letter of the specified position. #1 is the first item.",
        "helpUrl": ""
      },
      // Operators <string> contains <substring> block
      {
        "type": "operators_string_contains",
        "message0": "%1 contains %2 %3 ?",
        "args0": [
          {
            "type": "input_value",
            "name": "word",
            "check": "String"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "subword",
            "check": "String"
          }
        ],
        "inputsInline": true,
        "output": "Boolean",
        "colour": 120,
        "tooltip": "Returns true if the second string is in the first string.",
        "helpUrl": ""
      },
      // Operators logical AND block 
      {
        "type": "operators_and",
        "message0": "%1 and %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "a",
            "check": "Boolean"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "b",
            "check": "Boolean"
          }
        ],
        "output": "Boolean",
        "colour": 120,
        "tooltip": "Returns true if both inputs are true.",
        "helpUrl": ""
      },
      // Operators logical OR block 
      {
        "type": "operators_or",
        "message0": "%1 or %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "a",
            "check": "Boolean"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "b",
            "check": "Boolean"
          }
        ],
        "output": "Boolean",
        "colour": 120,
        "tooltip": "Returns true if at least one of the inputs is true.",
        "helpUrl": ""
      },
      // Operators round up block
      {
        "type": "operators_round",
        "message0": "round %1 %2",
        "args0": [
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "a",
            "check": "Number"
          }
        ],
        "inputsInline": true,
        "output": "Number",
        "colour": 120,
        "tooltip": "Round a number up.",
        "helpUrl": ""
      },
      // Operators pick random int block
      {
        "type": "operators_random_int",
        "message0": "pick random %1 %2 to %3 %4",
        "args0": [
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "a",
            "check": "Number"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "b",
            "check": "Number"
          }
        ],
        "output": "Number",
        "colour": 120,
        "tooltip": "Return a random integer between the two numbers (inclusive).",
        "helpUrl": ""
      },
      // Sensing ask and wait block
      {
        "type": "sensing_ask_and_wait",
        "message0": "ask %1 %2 and wait",
        "args0": [
          {
            "type": "input_dummy"
          },
          {
            "type": "input_value",
            "name": "question",
            "check": "String"
          }
        ],
        "inputsInline": true,
        "output": "String",
        "colour": 180,
        "tooltip": "Ask user for some text.",
        "helpUrl": ""
      },
      // Controls if, then block
      {
        "type": "controls_if_then",
        "message0": "if %1 then %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "condition",
            "check": "Boolean"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_statement",
            "name": "body"
          }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": 30,
        "tooltip": "",
        "helpUrl": ""
      },
      // Controls, if, then, else block
      {
        "type": "controls_if_then_else",
        "message0": "if %1 then %2 %3 else %4 %5",
        "args0": [
          {
            "type": "input_value",
            "name": "condition",
            "check": "Boolean"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_statement",
            "name": "body_1"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_statement",
            "name": "body_2"
          }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": 30,
        "tooltip": "",
        "helpUrl": ""
      },
      // Controls stop block
      {
        "type": "controls_stop",
        "message0": "stop",
        "previousStatement": null,
        "colour": 15,
        "tooltip": "Stops the containing loop.",
        "helpUrl": ""
      },
      // Controls repeat block
      {
        "type": "controls_repeat_num_times",
        "message0": "repeat %1 %2 %3 %4",
        "args0": [
          {
            "type": "input_value",
            "name": "num",
            "check": "Number"
          },
          {
            "type": "input_dummy",
            "align": "RIGHT"
          },
          {
            "type": "input_statement",
            "name": "body"
          },
          {
            "type": "input_dummy",
            "align": "RIGHT"
          }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": 45,
        "tooltip": "Do some statements several times.",
        "helpUrl": ""
      },
      // Controls repeat until block
      {
        "type": "controls_repeat_until",
        "message0": "repeat until %1 %2 %3",
        "args0": [
          {
            "type": "input_value",
            "name": "condition",
            "check": "Boolean"
          },
          {
            "type": "input_dummy"
          },
          {
            "type": "input_statement",
            "name": "body"
          }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": 45,
        "tooltip": "Repeat a statement several times until a condition is met.",
        "helpUrl": ""
      }
    ]);

    // Operators pick random int block
    Blockly.JavaScript['operators_random_int'] = function(block) {
      var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC) || '0';
      var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_ATOMIC) || '0';
      var functionName = Blockly.JavaScript.provideFunction_(
        'mathRandomInt',
        ['function ' + Blockly.JavaScript.FUNCTION_NAME_PLACEHOLDER_ +
            '(a, b) {',
         '  if (a > b) {',
         '    // Swap a and b to ensure a is smaller.',
         '    var c = a;',
         '    a = b;',
         '    b = c;',
         '  }',
         '  return Math.floor(Math.random() * (b - a + 1) + a);',
         '}']);
         var code = functionName + '(' + value_a + ', ' + value_b + ')';
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_random_int'] = function(block) {
      Blockly.Python.definitions_['import_random'] = 'import random';
      var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_NONE);
      var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_NONE);
      var code = 'random.randint(' + value_a + ', ' + value_b + ')';
      return [code, Blockly.Python.ORDER_FUNCTION_CALL];
    };

    // Controls repeat until block
    Blockly.JavaScript['controls_repeat_until'] = function(block) {
      var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
      var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
      var code = 'while (!' + value_condition + ') {\n' + statements_body + '}\n';
      return code;
    };
    Blockly.Python['controls_repeat_until'] = function(block) {
      var value_condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC) || 'False';
      var statements_body = Blockly.Python.statementToCode(block, 'body') || '  pass';
      var code = 'while not ' + value_condition + ':\n' + statements_body + '\n';
      return code;
    };

    // Controls repeat block
    Blockly.JavaScript['controls_repeat_num_times'] = function(block) {
      var value_num = Blockly.JavaScript.valueToCode(block, 'num', Blockly.JavaScript.ORDER_ATOMIC) || '0';
      var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
      var code = 'for (var count = 0; count < ' + value_num + '; count++) {\n' + statements_body + '}\n';
      return code;
    };
    Blockly.Python['controls_repeat_num_times'] = function(block) {
      var value_num = Blockly.Python.valueToCode(block, 'num', Blockly.Python.ORDER_ATOMIC) || '0';
      var statements_body = Blockly.Python.statementToCode(block, 'body') || '  pass';

      var code = 'for count in range(' + value_num + '):\n' + statements_body + '\n';
      return code;
    };
    
    // Controls, if, then, else block
    Blockly.JavaScript['controls_if_then_else'] = function(block) {
      var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
      var statements_body_1 = Blockly.JavaScript.statementToCode(block, 'body_1');
      var statements_body_2 = Blockly.JavaScript.statementToCode(block, 'body_2');
      var code = 'if (' + value_condition + ') {\n' + statements_body_1 + '} else {\n' + statements_body_2 + '}\n';
      return code;
    };
    Blockly.Python['controls_if_then_else'] = function(block) {
      var value_condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC) || "False";
      var statements_body_1 = Blockly.Python.statementToCode(block, 'body_1');
      var statements_body_2 = Blockly.Python.statementToCode(block, 'body_2');

      if (statements_body_1 === "") {
        statements_body_1 = '  pass\n'; // 2 spaces for indentation in Python
      }
      if (statements_body_2 === "") {
        statements_body_2 = '  pass'; // 2 spaces for indentation in Python
      }

      // TODO: Assemble Python into code variable.
      var code = 'if ' + value_condition + ':\n' + statements_body_1 + 'else:\n' + statements_body_2 + '\n';
      return code;
    };

    // Controls if, then block
    Blockly.JavaScript['controls_if_then'] = function(block) {
      var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
      var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
      var code = 'if (' + value_condition + ') {\n' + statements_body + '}\n';
      return code;
    };
    Blockly.Python['controls_if_then'] = function(block) {
      var value_condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC) || "False";
      var statements_body = Blockly.Python.statementToCode(block, 'body');

      if (statements_body === "") {
        statements_body = '  pass\n';
      }

      var code = 'if ' + value_condition + ':\n' + statements_body + '\n';
      return code;
    };

    // Looks say block
    Blockly.JavaScript['looks_say'] = function(block) {
      var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
      var code = 'alert(' + value_value + ');\n';
      return code;
    };
    Blockly.Python['looks_say'] = function(block) {
      var value_value = Blockly.Python.valueToCode(block, 'value', Blockly.Python.ORDER_ATOMIC);
      var code = 'print(' + value_value + ')\n';
      return code;
    };

    // Operators round up block
    Blockly.JavaScript['operators_round'] = function(block) {
      var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC);
      var code = 'Math.round(' + value_a + ')';
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_round'] = function(block) {
      var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC);
      var code = 'round(' + value_a + ')';
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators logical OR block 
    Blockly.JavaScript['operators_or'] = function(block) {
      var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_LOGICAL_OR) || 'false';
      var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_LOGICAL_OR) || 'false';
      var code = value_a + ' || ' + value_b;
      return [code, Blockly.JavaScript.ORDER_LOGICAL_OR];
    };
    Blockly.Python['operators_or'] = function(block) {
      var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC) || 'False';
      var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC) || 'False';
      var code = value_a + ' or ' + value_b;
      return [code, Blockly.Python.ORDER_NONE];
    };


    // Operators logical AND block
    Blockly.JavaScript['operators_and'] = function(block) {
      var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
      var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
      var code = value_a + ' && ' + value_b;
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_and'] = function(block) {
      var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC) || 'False';
      var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC) || 'False';
      var code = value_a + ' and ' + value_b;
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Controls stop block
    Blockly.JavaScript['controls_stop'] = function(block) {
      var code = 'break;\n';
      return code;
    };
    Blockly.Python['controls_stop'] = function(block) {
      var code = 'break\n';
      return code;
    };

    // Sensing ask and wait block
    Blockly.JavaScript['sensing_ask_and_wait'] = function(block) {
      var value_question = Blockly.JavaScript.valueToCode(block, 'question', Blockly.JavaScript.ORDER_ATOMIC);
      var code = 'prompt(' + value_question + ');\n'
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['sensing_ask_and_wait'] = function(block) {
      var value_question = Blockly.Python.valueToCode(block, 'question', Blockly.Python.ORDER_ATOMIC);
      var code = 'input(' + value_question + ')\n';
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators <string> contains <substring> block
    Blockly.JavaScript['operators_string_contains'] = function(block) {
      var value_word = Blockly.JavaScript.valueToCode(block, 'word', Blockly.JavaScript.ORDER_ATOMIC);
      var value_subword = Blockly.JavaScript.valueToCode(block, 'subword', Blockly.JavaScript.ORDER_ATOMIC);
      var code = value_word + ".includes(" + value_subword + ")";
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_string_contains'] = function(block) {
      var value_word = Blockly.Python.valueToCode(block, 'word', Blockly.Python.ORDER_ATOMIC);
      var value_subword = Blockly.Python.valueToCode(block, 'subword', Blockly.Python.ORDER_ATOMIC);
      var code = value_subword + " in " + value_word;
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators letter <num> of <string> block
    Blockly.JavaScript['operators_letter_of'] = function(block) {
      var value_index = Blockly.JavaScript.valueToCode(block, 'index', Blockly.JavaScript.ORDER_ATOMIC) - 1; // subtract 1 since index starts from 0 in JS
      var value_word = Blockly.JavaScript.valueToCode(block, 'word', Blockly.JavaScript.ORDER_ATOMIC);
      var code = value_word + ".charAt(" + value_index + ")";
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_letter_of'] = function(block) {
      var value_index = Blockly.Python.valueToCode(block, 'index', Blockly.Python.ORDER_ATOMIC) - 1; // subtract 1 since index starts from 0 in Python
      var value_word = Blockly.Python.valueToCode(block, 'word', Blockly.Python.ORDER_ATOMIC);
      var code = value_word + "[" + value_index + "]";
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators join/concatenate string block
    Blockly.JavaScript['operators_join_string'] = function(block) {
      var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC);
      var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_ATOMIC);
      var code = value_a + ' + ' + value_b;
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_join_string'] = function(block) {
      var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC);
      var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC);
      var code = value_a + ' + ' + value_b;
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators modulo block
    Blockly.JavaScript['operators_modulo'] = function(block) {
      var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_MODULUS);
      var value_n = Blockly.JavaScript.valueToCode(block, 'n', Blockly.JavaScript.ORDER_MODULUS);
      var code = '(' + value_a + ' % ' + value_n + ' + ' + value_n + ')' + ' % ' +  value_a;
      return [code, Blockly.JavaScript.ORDER_ADDITION];
    };
    Blockly.Python['operators_modulo'] = function(block) {
      var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC);
      var value_n = Blockly.Python.valueToCode(block, 'n', Blockly.Python.ORDER_ATOMIC);
      var code = value_a + ' % ' + value_n;
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators multiply block
    Blockly.JavaScript['operators_multiply'] = function(block) {
      var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_MULTIPLICATION);
      var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_MULTIPLICATION);
      var code = value_x + ' * ' + value_y;
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_multiply'] = function(block) {
      var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
      var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
      var code = value_x + ' * ' + value_y;
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators divide block
    Blockly.JavaScript['operators_divide'] = function(block) {
      var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
      var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
      var code = value_x + ' / ' + value_y;
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_divide'] = function(block) {
      var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
      var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
      var code = value_x + ' / ' + value_y;
      return [code, Blockly.Python.ORDER_NONE];
    };

    // Operators add block
    Blockly.JavaScript['operators_add'] = function(block) {
      var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
      var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
      var code = value_x + ' + ' + value_y;
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_add'] = function(block) {
      var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
      var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
      var code = value_x + ' + ' + value_y;
      return [code, Blockly.Python.ORDER_NONE];
    };
    
    // Operators subtract blocks
    Blockly.JavaScript['operators_subtract'] = function(block) {
      var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
      var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
      var code = value_x + ' - ' + value_y;
      return [code, Blockly.JavaScript.ORDER_NONE];
    };
    Blockly.Python['operators_subtract'] = function(block) {
      var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
      var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
      var code = value_x + ' - ' + value_y;
      return [code, Blockly.Python.ORDER_NONE];
    };



    const toolbox = document.getElementById('toolbox');
    /* Workspace configurations */
    const options = {
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
        startScale : 1,
        maxScale : 3,
        minScale : 0.3,
        scaleSpeed : 1.2
      }
    };
    /* Injects the blockly workspace */
    workspace = Blockly.inject('blocklyDiv', options);

    // Displays the user's previous submission 
    if (previous_submission) {
      // Decodes the previous_submission which contains HTML entities. Outputs a string, and it converts it to XML
      const xml_node = Blockly.Xml.textToDom(utils.decodeHTMLEntities(previous_submission))

      Blockly.Xml.domToWorkspace(xml_node, workspace);
    }
  })
}

/**
 * Retrieves code from the code mirror editor, runs all the test cases then updates the results table.
 * Disables the "CHECK" button and shows a loading spinner while request is being processed.
 */
function sendCodeToJobe() {
  let code = '';
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
  let raw_code;
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
  let code;
  if (programming_lang == "python") {
    code = myCodeMirror.getValue()
  } else {
    const lang = 'Python'
    code = Blockly[lang].workspaceToCode(workspace);
  }
  download(current_challenge_slug + ".py", code);
 }

/**
 * Retrieves the code from the blockly editor, converts it to JavaScript, runs the code.
 */
function runCode() { 
    // Convert blockly code to JavaScript
    const lang = 'JavaScript'
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
editorUtils.setupLessonNav()

// Save code when the user navigates using the next or prev buttons or opening nav
// Manually navigating to the next page to ensure code is saved first before the page reloads.
$("#prev_challenge_button").on("click", () => save_code().then(() => window.location.href = editorUtils.getPreviousChallengeURL()));
$("#next_challenge_button").on("click", () => save_code().then(() => window.location.href = editorUtils.getNextChallengeURL()));
$("#lessons_nav_toggle").on("click", () => save_code());
