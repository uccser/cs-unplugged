// Temporary testing variables
TEST_SOLUTION = "print('Hello World')"
TEST_INPUT = ""
TEST_OUTPUT = "Hello World"

// Set up code mirror
let myTextarea = document.getElementById("codemirror_editor");
let myCodeMirror = CodeMirror.fromTextArea(myTextarea, {
  lineNumbers: true,
  mode: "python",
  viewportMargin: Infinity
});

// Send code to jobe and get a result
function send_code_to_jobe() {
  let code = myCodeMirror.getValue()

  run_all_testcases(code, [TEST_INPUT], [TEST_OUTPUT]).then(result => {
    console.log('Result...')
    console.log(result);

    let jobeResult = document.getElementById("jobe_results");
    jobeResult.innerHTML = JSON.stringify(result);
  })
}

let submitButton = document.getElementById('editor_run_button');
submitButton.addEventListener("click", send_code_to_jobe)

