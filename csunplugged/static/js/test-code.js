const JOBE_SERVER = "http://localhost:4000/jobe/index.php/restapi/runs/";

async function run_code(program, givenInput, questionType) {
  let data = {
    run_spec: {
      language_id: "python3",
      sourcefilename: "test.py",
      sourcecode: program,
      input: givenInput ? questionType == "INPUT" : ""
    }
  };

  let response = await fetch(JOBE_SERVER, {
    method: "POST",
    headers: {
      "Content-type": "application/json; charset=utf-8",
      Accept: "application/json"
    },
    body: JSON.stringify(data)
  });

  let result = await response.json();
  return result;
}

async function run_testcase(userProgram, givenInput, expectedOutput, questionType) {
  if (questionType === "FUNCTION") {
    userProgram = userProgram.concat("\n" + givenInput)
  }

  let userResult = await run_code(userProgram, givenInput, questionType);

  testcaseResult = {
    status: "Passed",
    input: givenInput,
    userOutput: "",
    expectedOutput: expectedOutput
  };

  if (userResult.outcome == 15) {
    // Outcome 15: Run Successfully
    let userOutput = userResult.stdout.replace(/(\r\n|\n|\r)/gm, "");
    if (userOutput === expectedOutput || (givenInput && userOutput.includes(expectedOutput))) {
      testcaseResult.userOutput = userOutput;
    } else {
      testcaseResult.status = "Failed";
      testcaseResult.userOutput = userResult.stdout;
    }
  } else if (userResult.outcome == 11) {
    // Outcome 11: Compiler Error
    testcaseResult.status = "Compiler Error";
    testcaseResult.userOutput = userResult.cmpinfo;
  } else {
    // Any other error
    testcaseResult.status = "Error";
    testcaseResult.userOutput = userResult.stderr;
  }

  return testcaseResult;
}

async function run_all_testcases(userProgram, testCases) {
  allTestCaseResults = [];

  for (const testCase of testCases) {
    await run_testcase(
      userProgram,
      testCase.test_input,
      testCase.expected_output,
      testCase.questionType
    ).then(testcaseResult => {
      testcaseResult.id = testCase.id;
      allTestCaseResults.push(testcaseResult);
    });
  }

  return allTestCaseResults;
}
