// Scripts used to manage code running and testing for the programming challenge editor screen.

const JOBE_SERVER = jobe_proxy_url;

/**
 * Creates a request to the jobe proxy for the given program and input (if an 'input' question type). Recieves a response from jobe detailing if the code output
 * or if there was any errors.
 * @param {String} program The user code from the code mirror editor
 * @param {String} givenInput The given input for the test case being run.
 * @param {String} questionType The question type, used to determine whether the request should contain an 'input' field or not.
 * @return {Object} The response from the Jobe server.
 */
async function run_code(program, givenInput, questionType) {
  // Creates the run spec for Jobe
  let data = {
    run_spec: {
      language_id: "python3",
      sourcefilename: "test.py",
      sourcecode: program,
      input: questionType == "input" ? givenInput : ""
    }
  };

  // Sends request to the Jobe proxy and recieves a result.
  let response = await fetch(JOBE_SERVER, {
    method: "POST",
    headers: {
      "Content-type": "application/json; charset=utf-8",
      Accept: "application/json",
      "X-CSRFToken": csrf_token
    },
    body: JSON.stringify(data)
  });

  let result = await response.json();
  return result;
}

//
/**
 * Runs the code from the user program with some given input or function call.
 * Tests the output against some given expected output and returns a testCaseResult object.
 * @param {String} userProgram The user program from the code mirror editor.
 * @param {String} givenInput The given input or function call.
 * @param {String} expectedOutput The expected output for the given input.
 * @param {String} questionType Whether the question is either an 'input' type or a 'function' type. This changes how the code is run.
 * @return {Object} A test case result detailing if the code passed or if there was an error, the given input, user code output and expected output.
 */
async function run_testcase(
  userProgram,
  givenInput,
  expectedOutput,
  questionType
) {
  // Appends a function call to the end of the user call to test function type questions.
  if (questionType === "function") {
    userProgram = userProgram.concat("\n" + givenInput);
  }

  // Send code to Jobe to get the code output.
  let userResult = await run_code(userProgram, givenInput, questionType);

  // Test case result template
  testcaseResult = {
    status: "Passed",
    input: givenInput,
    userOutput: "",
    expectedOutput: expectedOutput,
    helpInfo: ""
  };

  if (userResult.outcome == 15) {
    // Outcome 15: Run Successfully
    let userOutput = userResult.stdout.replace(/\n$/, "");
    if (
      userOutput === expectedOutput)
    {
      testcaseResult.userOutput = userOutput;
    } else {
      testcaseResult.status = "Failed";
      testcaseResult.userOutput = userResult.stdout;
      testcaseResult.helpInfo = gettext("Looks like your code was run successfully but didn’t match the expected output. Have a look at the ‘Expected Output’ and the 'Received Output’. See if you can spot the differences!");
    }
  } else if (userResult.outcome == 11) {
    // Outcome 11: Compiler Error from Jobe (this has been changed to Syntax Error for plugging it in)
    testcaseResult.status = "Syntax Error";
    testcaseResult.userOutput = userResult.cmpinfo;
    testcaseResult.helpInfo = gettext("Oops, looks like there’s a spelling mistake or wrong character in your code. Try looking and see if you can find it! It might be a missing (parentheses) or a missing “quote mark”.");
  } else if (userResult.outcome == 13) {
    // Outcome 13: Time limit exceeeded
    testcaseResult.status = "Time limit exceeded";
    testcaseResult.userOutput = userResult.cmpinfo;
    testcaseResult.helpInfo = gettext("Looks like your code took too long to run. Maybe you have an infinite loop somewhere in your code?");
  } else {
    // Any other error
    testcaseResult.status = "Error";
    testcaseResult.userOutput = userResult.stderr;
    testcaseResult.helpInfo = gettext("Something went wrong when we tried to run your code. Have a look at the error output and see if you can solve this mystery error.");
  }

  return testcaseResult;
}

/**
 * Runs all the test cases for the current challenge against the users program.
 * @param {String} userProgram The users code from the code mirror editor.
 * @param {Array} testCases A list of test case objects.
 * @return {Array} A list of all the test case results.
 */
async function run_all_testcases(userProgram, testCases) {
  allTestCaseResults = [];

  for (const testCase of testCases) {
    await run_testcase(
      userProgram,
      testCase.test_input,
      testCase.expected_output,
      testCase.question_type
    ).then(testcaseResult => {
      testcaseResult.id = testCase.id;
      allTestCaseResults.push(testcaseResult);
    });
  }

  return allTestCaseResults;
}

exports.run_all_testcases = run_all_testcases;
