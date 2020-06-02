var challenge_user_input;


$(document).ready(function() {
    challenge_user_input = $('#challenge-user-input');

    // Run when submit button is clicked.
    $('#submit-answer').click(function(){
        // Deactiviate button
        $(this).prop('disabled', true);

        // Get challenge number and user_answer.
        var user_answer = challenge_user_input.val();

        // If empty, display message
        if (user_answer) {
            var challenge_number = $('#challenge-pills-tabContent > .tab-pane.active').data('challenge-number');
            var result = checkAnswer(challenge_number, user_answer);
            // Display output
            if (result) {
                displayFeedback('correct');
                $(this).hide();
            } else {
                displayFeedback('incorrect');
            }
            // Log to database

        } else {
            displayFeedback('empty');
        }

        // Activate button
        $(this).prop('disabled', false);
    });

    $('#challenge-pills-tab .nav-link').click(function() {
        challenge_user_input.val('');
        displayFeedback();
        $('#submit-answer').show();
    });
});


function checkAnswer(challenge_number, user_answer) {
  /**
   * Check if user answer matches correct answer.
   * @param {integer} challenge_number - Number of current challenge.
   * @param {string} user_answer - Answer submitted by user.
   * @return {boolean} Boolean if answer is correct.
   */
    challenge_answer = challenges_json[challenge_number];
    user_answer = user_answer.toLowerCase().replace(/,\s/g, ',');
    return challenge_answer == user_answer;
};


function displayFeedback(status) {
    /**
     * Update feedback to reflect given status.
     * @param {string} status - Type of feedback to provide.
     */
    challenge_user_input.removeClass('is-valid is-invalid is-empty');
    if (status == 'correct') {
        challenge_user_input.addClass('is-valid');
    } else if (status == 'incorrect') {
        challenge_user_input.addClass('is-invalid');
    } else if (status == 'empty') {
        challenge_user_input.addClass('is-empty');
    }
};


function logAnswer() {

};
