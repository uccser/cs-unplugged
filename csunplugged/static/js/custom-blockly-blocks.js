function setupBlockly(Blockly, pythonGenerator) {

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
    "message0": "join %1 %2 and %3",
    "args0": [
        {
        "type": "input_dummy"
        },
        {
        "type": "input_value",
        "name": "a",
        },
        {
        "type": "input_value",
        "name": "b",
        }
    ],
    "inputsInline": true,
    "output": "String",
    "style":  "operators_blocks",
    "tooltip": "Returns the combination of two inputs as a string (this can join a number and string together).",
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

// Python code generator for Values boolean block
pythonGenerator.forBlock['values_boolean'] = function(block) {
    var dropdown_value = block.getFieldValue('VALUE');
    var code = (dropdown_value == 'TRUE') ? 'True' : 'False';
    return [code, pythonGenerator.ORDER_ATOMIC];
};

// Python code generator for Values number block
pythonGenerator.forBlock['values_number'] = function(block) {
    var code = Number(block.getFieldValue('NUM'));
    var order;
    if (code == Infinity) {
    code = 'float("inf")';
    order = pythonGenerator.ORDER_FUNCTION_CALL;
    } else if (code == -Infinity) {
    code = '-float("inf")';
    order = pythonGenerator.ORDER_UNARY_SIGN;
    } else {
    order = code < 0 ? pythonGenerator.ORDER_UNARY_SIGN :
            pythonGenerator.ORDER_ATOMIC;
    }
    return [code, order];
};

// Python code generator for Values string block
pythonGenerator.forBlock['values_string'] = function(block) {
    var code = pythonGenerator.quote_(block.getFieldValue('TEXT'));
    return [code, pythonGenerator.ORDER_ATOMIC];
};

// Python code generator for Operators length of block
pythonGenerator.forBlock['operators_length_of'] = function(block) {
    // Is the string null or array empty?
    var text = pythonGenerator.valueToCode(block, 'VALUE', pythonGenerator.ORDER_NONE) || '\'\'';
    return ['len(' + text + ')', pythonGenerator.ORDER_FUNCTION_CALL];
};

// Python code generator for Operators equality block
pythonGenerator.forBlock['operators_equality'] = function(block) {
    var order = pythonGenerator.ORDER_RELATIONAL;
    var value_a = pythonGenerator.valueToCode(block, 'A', order) || '0';
    var value_b = pythonGenerator.valueToCode(block, 'B', order) || '0';
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' == ' + value_b;
    return [code, order];
};

// Python code generator for Operators less than block
pythonGenerator.forBlock['operators_less_than'] = function(block) {
    var order = pythonGenerator.ORDER_RELATIONAL;
    var value_a = pythonGenerator.valueToCode(block, 'A', order);
    var value_b = pythonGenerator.valueToCode(block, 'B', order);
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' < ' + value_b;
    return [code, order];
};

// Python code generator for Operators greater than block
pythonGenerator.forBlock['operators_greater_than'] = function(block) {
    var order = pythonGenerator.ORDER_RELATIONAL;
    var value_a = pythonGenerator.valueToCode(block, 'A', order);
    var value_b = pythonGenerator.valueToCode(block, 'B', order);
    if (!value_a && !value_b) {
        value_a = '0';
        value_b = '0';
    }
    var code = value_a + ' > ' + value_b;
    return [code, order];
};

// Python code generator for Operators single operand block
pythonGenerator.forBlock['operators_single'] = function(block) {
    // Math operators with single operand.
    var operator = block.getFieldValue('OP');
    var code;
    var arg;

    pythonGenerator.definitions_['import_math'] = 'import math';
    if (operator == 'SIN' || operator == 'COS' || operator == 'TAN') {
    arg = pythonGenerator.valueToCode(block, 'NUM',
        pythonGenerator.ORDER_MULTIPLICATIVE) || '0';
    } else {
    arg = pythonGenerator.valueToCode(block, 'NUM',
        pythonGenerator.ORDER_NONE) || '0';
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
    return [code, pythonGenerator.ORDER_FUNCTION_CALL];
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
    return [code, pythonGenerator.ORDER_MULTIPLICATIVE];
};

// Python code generator for Operators logical NOT block
pythonGenerator.forBlock['operators_not'] = function(block) {
    var value_argument = pythonGenerator.valueToCode(block, 'argument', pythonGenerator.ORDER_LOGICAL_NOT) || 'True';
    var code = 'not ' + value_argument;
    return [code, pythonGenerator.ORDER_LOGICAL_NOT];
};

// Python code generator for Operators pick random int block
pythonGenerator.forBlock['operators_random_int'] = function(block) {
    pythonGenerator.definitions_['import_random'] = 'import random';
    var value_a = pythonGenerator.valueToCode(block, 'a', pythonGenerator.ORDER_NONE) || '0';
    var value_b = pythonGenerator.valueToCode(block, 'b', pythonGenerator.ORDER_NONE) || '0';
    var code = 'random.randint(' + value_a + ', ' + value_b + ')';
    return [code, pythonGenerator.ORDER_FUNCTION_CALL];
};

// Python code generator for Controls repeat until block
pythonGenerator.forBlock['controls_repeat_until'] = function(block) {
    var value_condition = pythonGenerator.valueToCode(block, 'condition', pythonGenerator.ORDER_ATOMIC) || 'False';
    var statements_body = pythonGenerator.statementToCode(block, 'body') || '  pass';
    var code = 'while not ' + value_condition + ':\n' + statements_body + '\n';
    return code;
};

// Python code generator for Controls repeat block
pythonGenerator.forBlock['controls_repeat_num_times'] = function(block) {
    var value_num = pythonGenerator.valueToCode(block, 'num', pythonGenerator.ORDER_ATOMIC) || '0';
    var statements_body = pythonGenerator.statementToCode(block, 'body') || '  pass';

    var code = 'for count in range(' + value_num + '):\n' + statements_body + '\n';
    return code;
};

// Python code generator for Controls, if, then, else block
pythonGenerator.forBlock['controls_if_then_else'] = function(block) {
    var value_condition = pythonGenerator.valueToCode(block, 'condition', pythonGenerator.ORDER_ATOMIC) || "False";
    var statements_body_1 = pythonGenerator.statementToCode(block, 'body_1');
    var statements_body_2 = pythonGenerator.statementToCode(block, 'body_2');

    if (statements_body_1 === "") {
    statements_body_1 = '  pass\n'; // 2 spaces for indentation in Python
    }
    if (statements_body_2 === "") {
    statements_body_2 = '  pass'; // 2 spaces for indentation in Python
    }

    var code = 'if ' + value_condition + ':\n' + statements_body_1 + 'else:\n' + statements_body_2 + '\n';
    return code;
};

// Python code generator for Controls if, then block
pythonGenerator.forBlock['controls_if_then'] = function(block) {
    var value_condition = pythonGenerator.valueToCode(block, 'condition', pythonGenerator.ORDER_ATOMIC) || "False";
    var statements_body = pythonGenerator.statementToCode(block, 'body');

    if (statements_body === "") {
    statements_body = '  pass\n';
    }

    var code = 'if ' + value_condition + ':\n' + statements_body + '\n';
    return code;
};

// Python code generator for Looks say block
pythonGenerator.forBlock['looks_say'] = function(block) {
    var value_value = pythonGenerator.valueToCode(block, 'value', pythonGenerator.ORDER_ATOMIC) || '\'\'';
    var code = 'print(' + value_value + ')\n';
    return code;
};


// Python code generator for Operators round up block
pythonGenerator.forBlock['operators_round'] = function(block) {
    var value_a = pythonGenerator.valueToCode(block, 'a', pythonGenerator.ORDER_ATOMIC) || '0';
    var code = 'round(' + value_a + ')';
    return [code, pythonGenerator.ORDER_NONE];
};


// Python code generator for Operators logical OR block
pythonGenerator.forBlock['operators_or'] = function(block) {
    var value_a = pythonGenerator.valueToCode(block, 'a', pythonGenerator.ORDER_ATOMIC) || 'False';
    var value_b = pythonGenerator.valueToCode(block, 'b', pythonGenerator.ORDER_ATOMIC) || 'False';
    var code = value_a + ' or ' + value_b;
    return [code, pythonGenerator.ORDER_NONE];
};


// Python code generator for Operators logical AND block
pythonGenerator.forBlock['operators_and'] = function(block) {
    var value_a = pythonGenerator.valueToCode(block, 'a', pythonGenerator.ORDER_ATOMIC) || 'False';
    var value_b = pythonGenerator.valueToCode(block, 'b', pythonGenerator.ORDER_ATOMIC) || 'False';
    var code = value_a + ' and ' + value_b;
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Controls stop block
pythonGenerator.forBlock['controls_stop'] = function(block) {
    var code = 'break\n';
    return code;
};

// Python code generator for Sensing ask and wait number block
pythonGenerator.forBlock['sensing_ask_and_wait_number'] = function(block) {
    var functionName = pythonGenerator.provideFunction_(
        'text_prompt',
        ['def ' + pythonGenerator.FUNCTION_NAME_PLACEHOLDER_ + '(msg):',
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
        var msg = pythonGenerator.quote_(block.getFieldValue('question'));
    } else {
        // External message.
        var msg = pythonGenerator.valueToCode(block, 'question', pythonGenerator.ORDER_NONE) || '\'\'';
    }
    msg = '""' // Replaces user input parameters to be blank so it matches the expected output
    var code = functionName + '(' + msg + ')';
    return [code, pythonGenerator.ORDER_FUNCTION_CALL];
};

// Python code generator for Sensing ask and wait text block
pythonGenerator.forBlock['sensing_ask_and_wait_text'] = function(block) {
    var functionName = pythonGenerator.provideFunction_(
        'text_prompt',
        ['def ' + pythonGenerator.FUNCTION_NAME_PLACEHOLDER_ + '(msg):',
            '  try:',
            '    return raw_input(msg)',
            '  except NameError:',
            '    return input(msg)']);
        if (block.getField('question')) {
            // Internal message.
            var msg = pythonGenerator.quote_(block.getFieldValue('question'));
        } else {
            // External message.
            var msg = pythonGenerator.valueToCode(block, 'question', pythonGenerator.ORDER_NONE) || '\'\'';
        }
        msg = '""' // Replaces user input parameters to be blank so it matches the expected output
        var code = functionName + '(' + msg + ')';

    return [code, pythonGenerator.ORDER_FUNCTION_CALL];
  };

// Python code generator for Operators <string> contains <substring> block
pythonGenerator.forBlock['operators_string_contains'] = function(block) {
    var value_word = pythonGenerator.valueToCode(block, 'word', pythonGenerator.ORDER_ATOMIC) || '\'\'';
    var value_subword = pythonGenerator.valueToCode(block, 'subword', pythonGenerator.ORDER_ATOMIC) || '\'\'';
    var code = value_subword + " in " + value_word;
    return [code, pythonGenerator.ORDER_NONE];
};


// Python code generator for Operators letter <num> of <string> block
pythonGenerator.forBlock['operators_letter_of'] = function(block) {
    var value_index = pythonGenerator.valueToCode(block, 'index', pythonGenerator.ORDER_ATOMIC);
    var value_word = pythonGenerator.valueToCode(block, 'word', pythonGenerator.ORDER_ATOMIC) || '\'\'';
    value_index = parseInt(value_index)
    if (value_index) {
        // subtract 1 since index starts from 0 in Python
        value_index = value_index - 1;
    } else {
        // if index is falsy then default it to 0
        value_index = 0
    }
    var code = value_word + "[" + value_index + "]";
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Operators join/concatenate string block
pythonGenerator.forBlock['operators_join_string'] = function(block) {
    var value_a = pythonGenerator.valueToCode(block, 'a', pythonGenerator.ORDER_ATOMIC) || '\'\'';
    var value_b = pythonGenerator.valueToCode(block, 'b', pythonGenerator.ORDER_ATOMIC) || '\'\'';
    var code = 'str(' + value_a + ') + str(' + value_b + ')';
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Operators modulo block
pythonGenerator.forBlock['operators_modulo'] = function(block) {
    var value_a = pythonGenerator.valueToCode(block, 'a', pythonGenerator.ORDER_ATOMIC);
    var value_n = pythonGenerator.valueToCode(block, 'n', pythonGenerator.ORDER_ATOMIC);
    if (!value_a && !value_n) {
        value_a = '0';
        value_n = '1';
    }
    var code = value_a + ' % ' + value_n;
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Operators multiply block
pythonGenerator.forBlock['operators_multiply'] = function(block) {
    var value_x = pythonGenerator.valueToCode(block, 'x', pythonGenerator.ORDER_ATOMIC) || '0';
    var value_y = pythonGenerator.valueToCode(block, 'y', pythonGenerator.ORDER_ATOMIC) || '0';
    var code = value_x + ' * ' + value_y;
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Operators divide block
pythonGenerator.forBlock['operators_divide'] = function(block) {
    var value_x = pythonGenerator.valueToCode(block, 'x', pythonGenerator.ORDER_ATOMIC) || '0';
    var value_y = pythonGenerator.valueToCode(block, 'y', pythonGenerator.ORDER_ATOMIC) || '0';
    var functionName = pythonGenerator.provideFunction_(
        'divideNumber',
        ['def ' + pythonGenerator.FUNCTION_NAME_PLACEHOLDER_ + '(x, y):',
            '  return int(x/y) if (x/y).is_integer() else (x/y)']);
    var code = functionName + '(' + value_x + ', ' + value_y + ')';
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Operators add block
pythonGenerator.forBlock['operators_add'] = function(block) {
    var value_x = pythonGenerator.valueToCode(block, 'x', pythonGenerator.ORDER_ATOMIC) || '0';
    var value_y = pythonGenerator.valueToCode(block, 'y', pythonGenerator.ORDER_ATOMIC) || '0';
    var code = value_x + ' + ' + value_y;
    return [code, pythonGenerator.ORDER_NONE];
};

// Python code generator for Operators subtract blocks
pythonGenerator.forBlock['operators_subtract'] = function(block) {
    var value_x = pythonGenerator.valueToCode(block, 'x', pythonGenerator.ORDER_ATOMIC) || '0';
    var value_y = pythonGenerator.valueToCode(block, 'y', pythonGenerator.ORDER_ATOMIC) || '0';
    var code = value_x + ' - ' + value_y;
    return [code, pythonGenerator.ORDER_NONE];
};

}

module.exports = setupBlockly
