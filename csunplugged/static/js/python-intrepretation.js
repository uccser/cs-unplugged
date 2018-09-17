    function configurations(){
      Sk.configure({
        output: outputFunction,
        read: builtinRead,
        inputfun: sInput,
        inputfunTakesPrompt: true,
        python3: true
      });

      $('#console').empty();
    }

    function builtinRead(x) {
      if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
      return Sk.builtinFiles["files"][x];
    }

    function initiateconsole() {
      window.jqconsole = $('#console').jqconsole();
      jqconsole.SetPromptLabel('>>> ');
      jqconsole.Enable()
    };

    function startPrompt() {
      jqconsole.Prompt(true, function (input) {
          startPrompt();
        });
    };

    function outputFunction(text) {
      jqconsole.Write(text);
    };

    function runit() {
      configurations();
      initiateconsole();

      var sourceCode = document.getElementById("inputField").value; 

      var myPromise = Sk.misceval.asyncToPromise(function() {
        return Sk.importMainWithBody("<stdin>", false, sourceCode, true);
      });

      myPromise.then(function(mod) {
          startPrompt();
          jqconsole.Disable()
      },
        function(err) {
          console.log(err.toString());
      });
    } 

    function sInput() {
      return new Promise(function(resolve,reject) {
        jqconsole.Input(function(input){
          resolve(input);
        })
      })
    }

    window.onload = function(){
      runit();
    }