var challenge_number;

$(document).ready(function() {
    challenge_number = $('#challenge-pills-tabContent > .tab-pane.active').data('challenge-number');
    var challenge_user_input = $('#challenge-user-input-' + challenge_number);
    var submit_answer_button = $('#submit-answer-' + challenge_number);

    // Run when submit button is clicked.
    $('.submit-btn').click(function(){
        submitUserAnswer(challenge_number);
    });

    // Run when enter is pressed in input box.
    $('.user-input').keyup(function (e) {
        if (e.keyCode === 13) {
            submitUserAnswer(challenge_number);
        }
    });

    $('#challenge-pills-tab .nav-link').click(function() {
        challenge_number = $(this).data('challenge-number');
        challenge_user_input = $('#challenge-user-input-' + challenge_number);
        submit_answer_button = $('#submit-answer-' + challenge_number);
        challenge_user_input.val('');
        challenge_user_input.prop('readonly', false);
        challenge_user_input.removeClass('is-valid is-invalid is-empty');
        submit_answer_button.show();
    });
});


function submitUserAnswer(challenge_number) {
    challenge_user_input = $('#challenge-user-input-' + challenge_number);
    submit_answer_button = $('#submit-answer-' + challenge_number);
    // Deactiviate button
    submit_answer_button.prop('disabled', true);

    // Get challenge number and user_answer.
    var user_answer = challenge_user_input.val().trim();

    // If empty, display message
    if (user_answer) {
        var result = checkAnswer(challenge_number, user_answer);
        // Display output
        if (result) {
            displayFeedback('correct', challenge_user_input);
            submit_answer_button.hide();
            challenge_user_input.prop('readonly', true);
        } else {
            displayFeedback('incorrect', challenge_user_input);
        }
        // Log to database
        logAnswer(activity_slug, challenge_number, user_answer, result)
    } else {
        displayFeedback('empty', challenge_user_input);
    }

    // Activate button
    submit_answer_button.prop('disabled', false);
};


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


function displayFeedback(status, challenge_user_input) {
    /**
     * Update feedback to reflect given status.
     * @param {string} status - Type of feedback to provide.
     * @param {object} challenge_user_input - The challenge input box
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


function logAnswer(activity_slug, challenge_number, answer, correct) {
   /**
    * Log challenge submission to database.
    * @param {string} activity_slug - Slug of activity.
    * @param {integer} challenge_number - Number of current challenge.
    * @param {string} answer - Answer submitted by user.
    * @param {boolean} correct - Boolean if answer is correct.
    */
    var data = {
        activity_slug: activity_slug,
        challenge_number: challenge_number,
        answer: answer,
        correct: correct,
    };
    $.ajax({
        url: response_url,
        type: 'POST',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        headers: { "X-CSRFToken": csrf_token },
        dataType: 'json',
    });
};
