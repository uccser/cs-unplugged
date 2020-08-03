// Scripts used to manage the UI functionality for the programming challenge editor options bar.

/**
 * Opens the challenge navigation drawer. 
 */
function openNav() {
  const width_val = Math.min(window.innerWidth, 800); // The side drawer should be 100% if it is smaller than 800
  document.getElementById("my_sidenav").style.width = `${width_val}px`;
  document.getElementById("sidebar_overlay").style.zIndex = "1029";
  document.getElementById("sidebar_overlay").style.opacity = "0.6";
}

/**
 * Closes the challenge navigation drawer.
 */
function closeNav() {
  document.getElementById("my_sidenav").style.width = "0";
  document.getElementById("sidebar_overlay").style.zIndex = "0";
  document.getElementById("sidebar_overlay").style.opacity = "0";
}

// Setting up event listener for opening the navigation bar.
$("#lessons_nav_toggle").click(openNav);

// Setting up event listener for closing the navigation drawer.
$("#sidebar_overlay").click(closeNav);
$("#close_nav_button").click(closeNav);

/**
 * Sets the link to the next challenge if it is not the last challenge.
 * @param {Number} index The index of the current challenge
 */
function setNextChallenge(index) {
  if (index !== programming_exercises.length-1) {
    const nextLesson = programming_exercises[index+1];
    const nextLessonUrl = lesson_url + nextLesson.slug;
    $("#next_challenge_button").attr("href", nextLessonUrl);
  }
}

/**
 * Sets the link to the previous challenge if it is not the first challenge.
 * @param {Number} index The index of the current challenge
 */
function setPreviousChallenge(index) {
  if (index !== 0) {
    const prevLesson = programming_exercises[index-1];
    const prevLessonUrl = lesson_url + prevLesson.slug;
    $("#prev_challenge_button").attr("href", prevLessonUrl);
  }
}

/**
 * Sets up the links to the next and previous exercises.
 * Also sets the text to show lesson progression.
 */
function setupLessonNav() {
  const isCurrentChallengeIndex = (element) => element.slug == current_challenge_slug;
  currentChallengeIndex = programming_exercises.findIndex(isCurrentChallengeIndex);

  const progressionText = `Question <strong>${currentChallengeIndex+1}</strong> of <strong>${programming_exercises.length}</strong>`;
  document.getElementById("challenge_progression_text").innerHTML = progressionText;
  setPreviousChallenge(currentChallengeIndex)
  setNextChallenge(currentChallengeIndex)
}

// Apply the navigation setup
setupLessonNav()

// Add testing examples info to the requirements block (temporary)
const static_requirement_info = "Your program should display the outputs in the table (shown on the right) for the given inputs provided.";
$("#requirement + p").append(`</br></br> <p>${static_requirement_info}</p>`);
