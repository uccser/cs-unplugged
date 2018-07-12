  var base_url = "http://36adab90.compilers.sphere-engine.com/api/v3/submissions/";
  var token = "?access_token=5ec1d247f7d8b651411587faf1af080c";

  function sendCode() {
    $.ajax({
      type: "POST",
      url: base_url + token,
      data: {
        "language": 116,
        "sourceCode": editor.getValue(),
      },
      async: true,
      dataType: "json",
      success: function(result, status){
        id = result.id;
        setTimeout(function(){
          getCodeCompiled(id);
        }, 1000);
      },
      error: function(result, status){
        console.log("Error", result, status)
      }
    });
  };


 function getCodeCompiled(id) {
  $.ajax({
    type: "GET",
    url: base_url + id + token,
    data: {
        "withSource": true,
        "withOutput": true,
    },
    async: true,
    dataType: "json",
    success: function(result, status){
      if (result.status !== 0) {
        setTimeout(function(){
          getCodeCompiled(id);
        }, 1000);
      } else {
        outputBox.getDoc().setValue(result.output);
        if(isCorrectAnswer(result.output)){
            correctAnswerText();
          } else {
            incorrectAnswerText();
          }
      }
    },
    error: function(result, status){
      console.log("Error", result, status)
    }
  });
};


function isCorrectAnswer(user_output){
    var x = document.getElementsByClassName('codehilite')[0].innerHTML.substring(18,28) + '\n'; // TODO: CHANGE THIS LATER!
    console.log(x);
    return user_output === x;

};

function correctAnswerText(){
  document.getElementById("output-text").style.visibility = "visible";
  document.getElementById("output-text").className = "text-success";
  $("#output-text").html("Correct!");

}

function incorrectAnswerText(){
  document.getElementById("output-text").style.visibility = "visible";
  document.getElementById("output-text").className = "text-danger";
  $("#output-text").html("try again");
}