// Set up code mirror
let myTextarea = document.getElementById("codemirror_editor");
let myCodeMirror = CodeMirror.fromTextArea(myTextarea, {
  lineNumbers: true,
  mode: "python"
});

// Send code to jobe and get a result
function send_code_to_jobe() {
  let code = myCodeMirror.getValue()

  const data = {
    "run_spec": {
      "language_id": "python3",
      "sourcefilename": "test.py",
      "sourcecode": code
    }
  };

  let jobeResult = document.getElementById("jobe_result")
  let jobeOutputText = document.getElementById("jobe_output")

  JOBE_SERVER = "http://localhost:4000/jobe/index.php/restapi/runs/";

  fetch(JOBE_SERVER, {
    method: "POST",
    headers: {
      "Content-type": "application/json; charset=utf-8",
      Accept: "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      console.log("Success:", data);
      if (data.stdout) {
        console.log('here')
        jobeResult.innerHTML = "SUCCESS!"
        jobeOutputText.innerHTML = data.stdout
      } else if (data.cmpinfo) {
        jobeResult.innerHTML = "COMPILE ERROR!"
        jobeOutputText.innerHTML = data.cmpinfo
      } else {
        jobeResult.innerHTML = "ERROR!"
        jobeOutputText.innerHTML = data.stderr
      }
      
    })
    .catch(error => {
      console.error("Error:", error);
      jobeResult.innerHTML = "ERROR!"
      jobeOutputText.innerHTML = data.stderr
    });
}

let submitButton = document.getElementById('editor_run_button');
submitButton.addEventListener("click", send_code_to_jobe)

