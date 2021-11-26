function setupBlockly(Blockly) {
    
// Custom block definitions that were created to look and act like Scratch blocks
Blockly.defineBlocksWithJsonArray([
    // Values boolean block
    {
    "type": "values_boolean",
    "message0": "%1",
    "args0": [
        {
        "type": "field_dropdown",
        "name": "VALUE",
        "options": [
            [
            "true",
            "TRUE"
            ],
            [
            "false",
            "FALSE"
            ]
        ]
        }
    ],
    "output": "Boolean",
    "style":  "values_blocks",
    "tooltip": "Returns either true or false.",
    "helpUrl": ""
    },
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
    "style":  "looks_blocks",
    "tooltip": "Say the specified text, number or other value.",
    "helpUrl": ""
    },
    // Values number block
    {
    "type": "values_number",
    "message0": "%1",
    "args0": [{
        "type": "field_number",
        "name": "NUM",
        "value": 0
    }],
    "output": "Number",
    "helpUrl": "",
    "style":  "values_blocks",
    "tooltip": "A number.",
    "extensions": ["parent_tooltip_when_inline"]
    },
    // Values text block
    {
    "type": "values_string",
    "message0": "%1",
    "args0": [{
        "type": "field_input",
        "name": "TEXT",
        "text": ""
    }],
    "output": "String",
    "style":  "values_blocks",
    "helpUrl": "",
    "tooltip": "A letter, word, or a line or text.",
    "extensions": [
        "text_quotes",
        "parent_tooltip_when_inline"
    ]
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
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
    "tooltip": "Returns a combination of the two input strings added together.",
    "helpUrl": ""
    },
    // Operators letter <num> of <string> block
    {
    "type": "operators_letter_of",
    "message0": "letter %1 of %2",
    "args0": [
        {
        "type": "input_value",
        "name": "index",
        "check": "Number"
        },
        {
        "type": "input_value",
        "name": "word",
        "check": "String"
        }
    ],
    "inputsInline": true,
    "output": "String",
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
    "tooltip": "Returns true if the second string is in the first string.",
    "helpUrl": ""
    },
    // Operators length of
    {
    "type": "operators_length_of",
    "message0": "length of %1 %2",
    "args0": [
        {
        "type": "input_value",
        "name": "VALUE",
        "check": "String"
        },
        {
        "type": "input_dummy"
        }
    ],
    "output": "Number",
    "style":  "operators_blocks",
    "tooltip": "",
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
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
    "tooltip": "Returns true if at least one of the inputs is true.",
    "helpUrl": ""
    },
    // Operators logical NOT block
    {
    "type": "operators_not",
    "message0": "not %1 %2",
    "args0": [
        {
        "type": "input_value",
        "name": "argument",
        "check": "Boolean"
        },
        {
        "type": "input_dummy"
        }
    ],
    "output": "Boolean",
    "style":  "operators_blocks",
    "tooltip": "Return true if the input is false. Returns false if the input is true.",
    "helpUrl": ""
    },
    // Operators round up block
    {
    "type": "operators_round",
    "message0": "round %1",
    "args0": [
        {
        "type": "input_value",
        "name": "a",
        "check": "Number"
        }
    ],
    "inputsInline": true,
    "output": "Number",
    "style":  "operators_blocks",
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
    "style":  "operators_blocks",
    "tooltip": "Return a random integer between the two numbers (inclusive).",
    "helpUrl": ""
    },
    // Operators single operand block
    {
    "type": "operators_single",
    "message0": "%1 of %2 %3",
    "args0": [
        {
        "type": "field_dropdown",
        "name": "OP",
        "options": [
            [
            "abs",
            "ABS"
            ],
            [
            "floor",
            "FLOOR"
            ],
            [
            "ceiling",
            "CEIL"
            ],
            [
            "sqrt",
            "ROOT"
            ],
            [
            "sin",
            "SIN"
            ],
            [
            "cos",
            "COS"
            ],
            [
            "tan",
            "TAN"
            ],
            [
            "asin",
            "ASIN"
            ],
            [
            "acos",
            "ACOS"
            ],
            [
            "atan",
            "ATAN"
            ],
            [
            "ln",
            "LN"
            ],
            [
            "log",
            "LOG10"
            ],
            [
            "e ^",
            "EXP"
            ],
            [
            "10 ^",
            "POW10"
            ]
        ]
        },
        {
        "type": "input_value",
        "name": "NUM",
        "check": "Number",
        "align": "RIGHT"
        },
        {
        "type": "input_dummy"
        }
    ],
    "output": "Number",
    "style":  "operators_blocks",
    "tooltip": "Block for advanced math operators with single operand.",
    "helpUrl": ""
    },
    // Operators greater than block
    {
    "type": "operators_greater_than",
    "message0": "%1 > %2 %3",
    "args0": [
        {
        "type": "input_value",
        "name": "A"
        },
        {
        "type": "input_dummy"
        },
        {
        "type": "input_value",
        "name": "B"
        }
    ],
    "inputsInline": true,
    "output": "Boolean",
    "style":  "operators_blocks",
    "tooltip": "Return true if the first input is greater than the second input.",
    "helpUrl": ""
    },
    // Operators less than block
    {
    "type": "operators_less_than",
    "message0": "%1 < %2 %3",
    "args0": [
        {
        "type": "input_value",
        "name": "A"
        },
        {
        "type": "input_dummy"
        },
        {
        "type": "input_value",
        "name": "B"
        }
    ],
    "output": "Boolean",
    "style":  "operators_blocks",
    "tooltip": "Return true if the second input is greater than the first input.",
    "helpUrl": ""
    },
    // Operators equality block
    {
    "type": "operators_equality",
    "message0": "%1 = %2 %3",
    "args0": [
        {
        "type": "input_value",
        "name": "A"
        },
        {
        "type": "input_dummy"
        },
        {
        "type": "input_value",
        "name": "B"
        }
    ],
    "inputsInline": true,
    "output": "Boolean",
    "style":  "operators_blocks",
    "tooltip": "Return true if both inputs equal each other.",
    "helpUrl": ""
    },
    // Sensing ask and wait number block
    {
        "type": "sensing_ask_and_wait_number",
        "message0": "ask %1 %2 and wait for number",
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
        "output": "Number",
        "style":  "sensing_blocks",
        "tooltip": "Ask user for some number.",
        "helpUrl": ""
    },
    // Sensing ask and wait text block
    {
        "type": "sensing_ask_and_wait_text",
        "message0": "ask %1 %2 and wait for text",
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
        "style":  "sensing_blocks",
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
    "style":  "control_blocks",
    "tooltip": "If value is true, then do some statements.",
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
    "style":  "control_blocks",
    "tooltip": "If value is true, then do the first set of statements, else do the second set of statements",
    "helpUrl": ""
    },
    // Controls stop block
    {
    "type": "controls_stop",
    "message0": "stop",
    "previousStatement": null,
    "style":  "control_blocks",
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
    "style":  "control_blocks",
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
    "style":  "control_blocks",
    "tooltip": "Repeat a statement several times until a condition is met.",
    "helpUrl": ""
    }
]);

// JavaScript code generator for Values boolean block
Blockly.JavaScript['values_boolean'] = function(block) {
    var dropdown_value = block.getFieldValue('VALUE');
    var code = (dropdown_value == 'TRUE') ? 'true' : 'false';
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
};
// Python code generator for Values boolean block
Blockly.Python['values_boolean'] = function(block) {
    var dropdown_value = block.getFieldValue('VALUE');
    var code = (dropdown_value == 'TRUE') ? 'True' : 'False';
    return [code, Blockly.Python.ORDER_ATOMIC];
};

// JavaScript code generator for Values number block
Blockly.JavaScript['values_number'] = function(block) {
    var code = Number(block.getFieldValue('NUM'));
    var order = code >= 0 ? Blockly.JavaScript.ORDER_ATOMIC : Blockly.JavaScript.ORDER_UNARY_NEGATION;
    return [code, order];
};
// Python code generator for Values number block
Blockly.Python['values_number'] = function(block) {
    var code = Number(block.getFieldValue('NUM'));
    var order;
    if (code == Infinity) {
    code = 'float("inf")';
    order = Blockly.Python.ORDER_FUNCTION_CALL;
    } else if (code == -Infinity) {
    code = '-float("inf")';
    order = Blockly.Python.ORDER_UNARY_SIGN;
    } else {
    order = code < 0 ? Blockly.Python.ORDER_UNARY_SIGN :
            Blockly.Python.ORDER_ATOMIC;
    }
    return [code, order];
};

// JavaScript code generator for Values string block
Blockly.JavaScript['values_string'] = function(block) {
    var code = Blockly.JavaScript.quote_(block.getFieldValue('TEXT'));
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
};
// Python code generator for Values string block
Blockly.Python['values_string'] = function(block) {
    var code = Blockly.Python.quote_(block.getFieldValue('TEXT'));
    return [code, Blockly.Python.ORDER_ATOMIC];
};

// JavaScript code generator for Operators length of block
Blockly.JavaScript['operators_length_of'] = function(block) {
    // String or array length.
    var text = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_MEMBER) || '\'\'';
    return [text + '.length', Blockly.JavaScript.ORDER_MEMBER];
};
// Python code generator for Operators length of block
Blockly.Python['operators_length_of'] = function(block) {
    // Is the string null or array empty?
    var text = Blockly.Python.valueToCode(block, 'VALUE', Blockly.Python.ORDER_NONE) || '\'\'';
    return ['len(' + text + ')', Blockly.Python.ORDER_FUNCTION_CALL];
};

// JavaScript code generator for Operators equality block
Blockly.JavaScript['operators_equality'] = function(block) {
    var order = Blockly.JavaScript.ORDER_RELATIONAL;
    var value_a = Blockly.JavaScript.valueToCode(block, 'A', order) || '0';
    var value_b = Blockly.JavaScript.valueToCode(block, 'B', order) || '0';
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' == ' + value_b;
    return [code, order];
};
// Python code generator for Operators equality block
Blockly.Python['operators_equality'] = function(block) {
    var order = Blockly.Python.ORDER_RELATIONAL;
    var value_a = Blockly.Python.valueToCode(block, 'A', order) || '0';
    var value_b = Blockly.Python.valueToCode(block, 'B', order) || '0';
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' == ' + value_b;
    return [code, order];
};


// JavaScript code generator for Operators less than block
Blockly.JavaScript['operators_less_than'] = function(block) {
    var order = Blockly.JavaScript.ORDER_RELATIONAL;
    var value_a = Blockly.JavaScript.valueToCode(block, 'A', order);
    var value_b = Blockly.JavaScript.valueToCode(block, 'B', order);
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' < ' + value_b;
    return [code, order];
};
// Python code generator for Operators less than block
Blockly.Python['operators_less_than'] = function(block) {
    var order = Blockly.Python.ORDER_RELATIONAL;
    var value_a = Blockly.Python.valueToCode(block, 'A', order);
    var value_b = Blockly.Python.valueToCode(block, 'B', order);
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' < ' + value_b;
    return [code, order];
};

// JavaScript code generator for Operators greater than block
Blockly.JavaScript['operators_greater_than'] = function(block) {
    var order = Blockly.JavaScript.ORDER_RELATIONAL;
    var value_a = Blockly.JavaScript.valueToCode(block, 'A', order);
    var value_b = Blockly.JavaScript.valueToCode(block, 'B', order);
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' > ' + value_b;
    return [code, order];
};
// Python code generator for Operators greater than block
Blockly.Python['operators_greater_than'] = function(block) {
    var order = Blockly.Python.ORDER_RELATIONAL;
    var value_a = Blockly.Python.valueToCode(block, 'A', order);
    var value_b = Blockly.Python.valueToCode(block, 'B', order);
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' > ' + value_b;
    return [code, order];
};

// JavaScript code generator for Operators single operand block
Blockly.JavaScript['operators_single'] = function(block) {
    // Math operators with single operand.
    var operator = block.getFieldValue('OP');
    var code;
    var arg;
    if (operator == 'SIN' || operator == 'COS' || operator == 'TAN') {
    arg = Blockly.JavaScript.valueToCode(block, 'NUM',
        Blockly.JavaScript.ORDER_DIVISION) || '0';
    } else {
    arg = Blockly.JavaScript.valueToCode(block, 'NUM',
        Blockly.JavaScript.ORDER_NONE) || '0';
    }
    // First, handle cases which generate values that don't need parentheses
    // wrapping the code.
    switch (operator) {
    case 'ABS':
        code = 'Math.abs(' + arg + ')';
        break;
    case 'FLOOR':
        code = 'Math.floor(' + arg + ')';
        break;
    case 'CEIL':
        code = 'Math.ceil(' + arg + ')';
        break;
    case 'ROOT':
        code = 'Math.sqrt(' + arg + ')';
        break;
    case 'SIN':
        code = 'Math.sin(' + arg + ' / 180 * Math.PI)';
        break;
    case 'COS':
        code = 'Math.cos(' + arg + ' / 180 * Math.PI)';
        break;
    case 'TAN':
        code = 'Math.tan(' + arg + ' / 180 * Math.PI)';
        break;
    case 'LN':
        code = 'Math.log(' + arg + ')';
        break;
    case 'EXP':
        code = 'Math.exp(' + arg + ')';
        break;
    case 'POW10':
        code = 'Math.pow(10,' + arg + ')';
        break;
    }
    if (code) {
    return [code, Blockly.JavaScript.ORDER_FUNCTION_CALL];
    }
    // Second, handle cases which generate values that may need parentheses
    // wrapping the code.
    switch (operator) {
    case 'LOG10':
        code = 'Math.log(' + arg + ') / Math.log(10)';
        break;
    case 'ASIN':
        code = 'Math.asin(' + arg + ') / Math.PI * 180';
        break;
    case 'ACOS':
        code = 'Math.acos(' + arg + ') / Math.PI * 180';
        break;
    case 'ATAN':
        code = 'Math.atan(' + arg + ') / Math.PI * 180';
        break;
    default:
        throw Error('Unknown math operator: ' + operator);
    }
    return [code, Blockly.JavaScript.ORDER_DIVISION];
};
// Python code generator for Operators single operand block
Blockly.Python['operators_single'] = function(block) {
    // Math operators with single operand.
    var operator = block.getFieldValue('OP');
    var code;
    var arg;
    
    Blockly.Python.definitions_['import_math'] = 'import math';
    if (operator == 'SIN' || operator == 'COS' || operator == 'TAN') {
    arg = Blockly.Python.valueToCode(block, 'NUM',
        Blockly.Python.ORDER_MULTIPLICATIVE) || '0';
    } else {
    arg = Blockly.Python.valueToCode(block, 'NUM',
        Blockly.Python.ORDER_NONE) || '0';
    }

    // First, handle cases which generate values that don't need parentheses
    // wrapping the code.
    switch (operator) {
    case 'ABS':
        code = 'math.fabs(' + arg + ')';
        break;
    case 'FLOOR':
        code = 'math.floor(' + arg + ')';
        break;
    case 'CEIL':
        code = 'math.ceil(' + arg + ')';
        break;
    case 'ROOT':
        code = 'math.sqrt(' + arg + ')';
        break;
    case 'SIN':
        code = 'math.sin(' + arg + ' / 180.0 * math.pi)';
        break;
    case 'COS':
        code = 'math.cos(' + arg + ' / 180.0 * math.pi)';
        break;
    case 'TAN':
        code = 'math.tan(' + arg + ' / 180.0 * math.pi)';
        break;
    case 'LN':
        code = 'math.log(' + arg + ')';
        break;
    case 'LOG10':
        code = 'math.log10(' + arg + ')';
        break;
    case 'EXP':
        code = 'math.exp(' + arg + ')';
        break;
    case 'POW10':
        code = 'math.pow(10,' + arg + ')';
        break;
    }
    if (code) {
    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
    }
    // Second, handle cases which generate values that may need parentheses
    // wrapping the code.
    switch (operator) {
    case 'ASIN':
        code = 'math.asin(' + arg + ') / math.pi * 180';
        break;
    case 'ACOS':
        code = 'math.acos(' + arg + ') / math.pi * 180';
        break;
    case 'ATAN':
        code = 'math.atan(' + arg + ') / math.pi * 180';
        break;
    default:
        throw Error('Unknown math operator: ' + operator);
    }
    return [code, Blockly.Python.ORDER_MULTIPLICATIVE];
};

// JavaScript code generator for Operators logical NOT block
Blockly.JavaScript['operators_not'] = function(block) {
    var value_argument = Blockly.JavaScript.valueToCode(block, 'argument', Blockly.JavaScript.ORDER_LOGICAL_NOT) || 'true';
    var code = '!' + value_argument;
    return [code, Blockly.JavaScript.ORDER_LOGICAL_NOT];
};
// Python code generator for Operators logical NOT block
Blockly.Python['operators_not'] = function(block) {
    var value_argument = Blockly.Python.valueToCode(block, 'argument', Blockly.Python.ORDER_LOGICAL_NOT) || 'True';
    var code = 'not ' + value_argument;
    return [code, Blockly.Python.ORDER_LOGICAL_NOT];
};

// JavaScript code generator for Operators pick random int block
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
// Python code generator for Operators pick random int block
Blockly.Python['operators_random_int'] = function(block) {
    Blockly.Python.definitions_['import_random'] = 'import random';
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_NONE) || '0';
    var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_NONE) || '0';
    var code = 'random.randint(' + value_a + ', ' + value_b + ')';
    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
};

// JavaScript code generator for Controls repeat until block
Blockly.JavaScript['controls_repeat_until'] = function(block) {
    var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
    var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
    var code = 'while (!' + value_condition + ') {\n' + statements_body + '}\n';
    return code;
};
// Python code generator for Controls repeat until block
Blockly.Python['controls_repeat_until'] = function(block) {
    var value_condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC) || 'False';
    var statements_body = Blockly.Python.statementToCode(block, 'body') || '  pass';
    var code = 'while not ' + value_condition + ':\n' + statements_body + '\n';
    return code;
};

// JavaScript code generator for Controls repeat block
Blockly.JavaScript['controls_repeat_num_times'] = function(block) {
    var value_num = Blockly.JavaScript.valueToCode(block, 'num', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
    var code = 'for (var count = 0; count < ' + value_num + '; count++) {\n' + statements_body + '}\n';
    return code;
};
// Python code generator for Controls repeat block
Blockly.Python['controls_repeat_num_times'] = function(block) {
    var value_num = Blockly.Python.valueToCode(block, 'num', Blockly.Python.ORDER_ATOMIC) || '0';
    var statements_body = Blockly.Python.statementToCode(block, 'body') || '  pass';

    var code = 'for count in range(' + value_num + '):\n' + statements_body + '\n';
    return code;
};

// JavaScript code generator for Controls, if, then, else block
Blockly.JavaScript['controls_if_then_else'] = function(block) {
    var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
    var statements_body_1 = Blockly.JavaScript.statementToCode(block, 'body_1');
    var statements_body_2 = Blockly.JavaScript.statementToCode(block, 'body_2');
    var code = 'if (' + value_condition + ') {\n' + statements_body_1 + '} else {\n' + statements_body_2 + '}\n';
    return code;
};
// Python code generator for Controls, if, then, else block
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

    var code = 'if ' + value_condition + ':\n' + statements_body_1 + 'else:\n' + statements_body_2 + '\n';
    return code;
};

// JavaScript code generator for Controls if, then block
Blockly.JavaScript['controls_if_then'] = function(block) {
    var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
    var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
    var code = 'if (' + value_condition + ') {\n' + statements_body + '}\n';
    return code;
};
// Python code generator for Controls if, then block
Blockly.Python['controls_if_then'] = function(block) {
    var value_condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC) || "False";
    var statements_body = Blockly.Python.statementToCode(block, 'body');

    if (statements_body === "") {
    statements_body = '  pass\n';
    }

    var code = 'if ' + value_condition + ':\n' + statements_body + '\n';
    return code;
};


/**
 * JavaScript code generator for Looks say block
 * 
 * This code generator was specifically created to handle how the output of the Say block is displayed
 * The JavaScript code returned by this function dynamically modifies the content of the console shell by 
 * using document.querySelector() to get the console shell, and then adding the content to it.
 * 
 * Therefore, if the ID of the console shell were to change, 
 * then this function needs to be changed as well in order for it to work!
 */
Blockly.JavaScript['looks_say'] = function(block) {
    var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC) || '\'\'';
    var functionName = Blockly.JavaScript.provideFunction_(
        'checkDataType',
        ['function ' + Blockly.JavaScript.FUNCTION_NAME_PLACEHOLDER_ +
            '(a) {',
            '  var type_a;',
            '  switch(typeof a){',
            '    case \'number\':',
            '      type_a = \'console-number\'',
            '      break',
            '    case \'boolean\':',
            '      type_a = \'console-boolean\'',
            '      break',
            '    default:',
            '      type_a = \'console-default\'',
            '  }',
            '  return type_a;',
            '}']);
    // if the value_value is an expression, then execute it first and put the output in a variable.
    var get_value = "var value = " + value_value + ";\n"
    var get_value_type = 'var value_type = ' + functionName + '(value);\n'
    var innerHTML_value = "'<span class=' + value_type + '>' + value + '</span><br/>'\n";
    var code = get_value + get_value_type + 'document.querySelector("#block-based-console-content").innerHTML += ' + innerHTML_value;
    return code;
};
// Python code generator for Looks say block
Blockly.Python['looks_say'] = function(block) {
    var value_value = Blockly.Python.valueToCode(block, 'value', Blockly.Python.ORDER_ATOMIC) || '\'\'';
    var code = 'print(' + value_value + ')\n';
    return code;
};

// JavaScript code generator for Operators round up block
Blockly.JavaScript['operators_round'] = function(block) {
    var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var code = 'Math.round(' + value_a + ')';
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators round up block
Blockly.Python['operators_round'] = function(block) {
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC) || '0';
    var code = 'round(' + value_a + ')';
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators logical OR block 
Blockly.JavaScript['operators_or'] = function(block) {
    var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_LOGICAL_OR) || 'false';
    var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_LOGICAL_OR) || 'false';
    var code = value_a + ' || ' + value_b;
    return [code, Blockly.JavaScript.ORDER_LOGICAL_OR];
};
// Python code generator for Operators logical OR block 
Blockly.Python['operators_or'] = function(block) {
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC) || 'False';
    var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC) || 'False';
    var code = value_a + ' or ' + value_b;
    return [code, Blockly.Python.ORDER_NONE];
};


// JavaScript code generator for Operators logical AND block
Blockly.JavaScript['operators_and'] = function(block) {
    var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
    var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_ATOMIC) || 'false';
    var code = value_a + ' && ' + value_b;
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators logical AND block
Blockly.Python['operators_and'] = function(block) {
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC) || 'False';
    var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC) || 'False';
    var code = value_a + ' and ' + value_b;
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Controls stop block
Blockly.JavaScript['controls_stop'] = function(block) {
    var code = 'break;\n';
    return code;
};
// Python code generator for Controls stop block
Blockly.Python['controls_stop'] = function(block) {
    var code = 'break\n';
    return code;
};

// JavaScript code generator for Sensing ask and wait number block
Blockly.JavaScript['sensing_ask_and_wait_number'] = function(block) {
    if (block.getField('question')) {
        // Internal message.
        var msg = Blockly.JavaScript.quote_(block.getFieldValue('question'));
    } else {
        // External message.
        var msg = Blockly.JavaScript.valueToCode(block, 'question', Blockly.JavaScript.ORDER_NONE) || '\'\'';
    }
    var code = 'Number(window.prompt(' + msg + '))';
    return [code, Blockly.JavaScript.ORDER_FUNCTION_CALL];
  };
// Python code generator for Sensing ask and wait number block
Blockly.Python['sensing_ask_and_wait_number'] = function(block) {
    var functionName = Blockly.Python.provideFunction_(
        'text_prompt',
        ['def ' + Blockly.Python.FUNCTION_NAME_PLACEHOLDER_ + '(msg):',
            '  try:',
            '    user_input = raw_input(msg)',
            '  except NameError:',
            '    user_input = input(msg)',
            '  finally:',
            '    if any(not c.isalnum() for c in user_input):',
            '      return float(user_input)',
            '    else:',
            '      return int(user_input)']);
    if (block.getField('question')) {
        // Internal message.
        var msg = Blockly.Python.quote_(block.getFieldValue('question'));
    } else {
        // External message.
        var msg = Blockly.Python.valueToCode(block, 'question', Blockly.Python.ORDER_NONE) || '\'\'';
    }
    msg = '""' // Replaces user input parameters to be blank so it matches the expected output
    var code = functionName + '(' + msg + ')';
    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
  };

// JavaScript code generator for Sensing ask and wait text block
Blockly.JavaScript['sensing_ask_and_wait_text'] = function(block) {
    if (block.getField('question')) {
        // Internal message.
        var msg = Blockly.JavaScript.quote_(block.getFieldValue('question'));
    } else {
        // External message.
        var msg = Blockly.JavaScript.valueToCode(block, 'question', Blockly.JavaScript.ORDER_NONE) || '\'\'';
    }
    var code = 'window.prompt(' + msg + ')';
    return [code, Blockly.JavaScript.ORDER_FUNCTION_CALL];
  };
// Python code generator for Sensing ask and wait text block
Blockly.Python['sensing_ask_and_wait_text'] = function(block) {
    var functionName = Blockly.Python.provideFunction_(
        'text_prompt',
        ['def ' + Blockly.Python.FUNCTION_NAME_PLACEHOLDER_ + '(msg):',
            '  try:',
            '    return raw_input(msg)',
            '  except NameError:',
            '    return input(msg)']);
        if (block.getField('question')) {
            // Internal message.
            var msg = Blockly.Python.quote_(block.getFieldValue('question'));
        } else {
            // External message.
            var msg = Blockly.Python.valueToCode(block, 'question', Blockly.Python.ORDER_NONE) || '\'\'';
        }
        msg = '""' // Replaces user input parameters to be blank so it matches the expected output
        var code = functionName + '(' + msg + ')';

    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
  };

// JavaScript code generator for Operators <string> contains <substring> block
Blockly.JavaScript['operators_string_contains'] = function(block) {
    var value_word = Blockly.JavaScript.valueToCode(block, 'word', Blockly.JavaScript.ORDER_ATOMIC) || '\'\'';
    var value_subword = Blockly.JavaScript.valueToCode(block, 'subword', Blockly.JavaScript.ORDER_ATOMIC) || '\'\'';
    var code = value_word + ".includes(" + value_subword + ")";
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators <string> contains <substring> block
Blockly.Python['operators_string_contains'] = function(block) {
    var value_word = Blockly.Python.valueToCode(block, 'word', Blockly.Python.ORDER_ATOMIC) || '\'\'';
    var value_subword = Blockly.Python.valueToCode(block, 'subword', Blockly.Python.ORDER_ATOMIC) || '\'\'';
    var code = value_subword + " in " + value_word;
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators letter <num> of <string> block
Blockly.JavaScript['operators_letter_of'] = function(block) {
    var value_index = Blockly.JavaScript.valueToCode(block, 'index', Blockly.JavaScript.ORDER_ATOMIC);
    var value_word = Blockly.JavaScript.valueToCode(block, 'word', Blockly.JavaScript.ORDER_ATOMIC) || '\'\'';
    value_index = parseInt(value_index)
    if (value_index) {
        // subtract 1 since index starts from 0 in Python
        value_index = value_index - 1;
    } else {
        // if index is falsy then default it to 0
        value_index = 0;
    }
    var code = value_word + ".charAt(" + value_index + ")";
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators letter <num> of <string> block
Blockly.Python['operators_letter_of'] = function(block) {
    var value_index = Blockly.Python.valueToCode(block, 'index', Blockly.Python.ORDER_ATOMIC); 
    var value_word = Blockly.Python.valueToCode(block, 'word', Blockly.Python.ORDER_ATOMIC) || '\'\'';
    value_index = parseInt(value_index)
    if (value_index) {
        // subtract 1 since index starts from 0 in Python
        value_index = value_index - 1;
    } else {
        // if index is falsy then default it to 0
        value_index = 0
    }
    var code = value_word + "[" + value_index + "]";
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators join/concatenate string block
Blockly.JavaScript['operators_join_string'] = function(block) {
    var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_ATOMIC) || '\'\'';
    var value_b = Blockly.JavaScript.valueToCode(block, 'b', Blockly.JavaScript.ORDER_ATOMIC) || '\'\'';
    var code = value_a + ' + ' + value_b;
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators join/concatenate string block
Blockly.Python['operators_join_string'] = function(block) {
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC) || '\'\'';
    var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC) || '\'\'';
    var code = value_a + ' + ' + value_b;
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators modulo block
Blockly.JavaScript['operators_modulo'] = function(block) {
    var value_a = Blockly.JavaScript.valueToCode(block, 'a', Blockly.JavaScript.ORDER_MODULUS);
    var value_n = Blockly.JavaScript.valueToCode(block, 'n', Blockly.JavaScript.ORDER_MODULUS);
    if (!value_a && !value_n) {
        value_a = '0';
        value_n = '1';
    }
    var code = '(' + value_a + ' % ' + value_n + ' + ' + value_n + ')' + ' % ' +  value_n;
    return [code, Blockly.JavaScript.ORDER_ADDITION];
};
// Python code generator for Operators modulo block
Blockly.Python['operators_modulo'] = function(block) {
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC);
    var value_n = Blockly.Python.valueToCode(block, 'n', Blockly.Python.ORDER_ATOMIC);
    if (!value_a && !value_n) {
        value_a = '0';
        value_n = '1';
    }
    var code = value_a + ' % ' + value_n;
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators multiply block
Blockly.JavaScript['operators_multiply'] = function(block) {
    var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_MULTIPLICATION) || '0';
    var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_MULTIPLICATION) || '0';
    var code = value_x + ' * ' + value_y;
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators multiply block
Blockly.Python['operators_multiply'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC) || '0';
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC) || '0';
    var code = value_x + ' * ' + value_y;
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators divide block
Blockly.JavaScript['operators_divide'] = function(block) {
    var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var code = value_x + ' / ' + value_y;
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators divide block
Blockly.Python['operators_divide'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC) || '0';
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC) || '0';
    var functionName = Blockly.Python.provideFunction_(
        'divideNumber',
        ['def ' + Blockly.Python.FUNCTION_NAME_PLACEHOLDER_ + '(x, y):',
            '  return int(x/y) if (x/y).is_integer() else (x/y)']);
    var code = functionName + '(' + value_x + ', ' + value_y + ')';
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators add block
Blockly.JavaScript['operators_add'] = function(block) {
    var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var code = value_x + ' + ' + value_y;
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators add block
Blockly.Python['operators_add'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC) || '0';
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC) || '0';
    var code = value_x + ' + ' + value_y;
    return [code, Blockly.Python.ORDER_NONE];
};

// JavaScript code generator for Operators subtract blocks
Blockly.JavaScript['operators_subtract'] = function(block) {
    var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC) || '0';
    var code = value_x + ' - ' + value_y;
    return [code, Blockly.JavaScript.ORDER_NONE];
};
// Python code generator for Operators subtract blocks
Blockly.Python['operators_subtract'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC) || '0';
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC) || '0';
    var code = value_x + ' - ' + value_y;
    return [code, Blockly.Python.ORDER_NONE];
};

}

module.exports = setupBlockly