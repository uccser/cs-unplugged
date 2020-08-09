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

/**
 * Gets the index of the current challenge.
 */
function getCurrentIndex() {
  const isCurrentChallengeIndex = (element) => element.slug == current_challenge_slug;
  return programming_exercises.findIndex(isCurrentChallengeIndex);
}

/**
 * Gets the link to the next challenge if it is not the last challenge.
 */
function getNextChallengeURL() {
  const index = getCurrentIndex();

  if (index !== programming_exercises.length-1) {
    const nextLesson = programming_exercises[index+1];
    return nextLessonUrl = lesson_url + nextLesson.slug;
  }

  return '#'
}

/**
 * Sets the link to the previous challenge if it is not the first challenge.
 */
function getPreviousChallengeURL() {
  const index = getCurrentIndex()

  if (index !== 0) {
    const prevLesson = programming_exercises[index-1];
    return prevLessonUrl = lesson_url + prevLesson.slug;
  }

  return "#"
}

/**
 * Sets up the links to the next and previous exercises.
 * Also sets the text to show lesson progression.
 */
function setupLessonNav() {
  // Setting up event listener for opening the navigation bar.
  $("#lessons_nav_toggle").click(openNav);

  // Setting up event listener for closing the navigation drawer.
  $("#sidebar_overlay").click(closeNav);
  $("#close_nav_button").click(closeNav);

  // Sets the question progression text.
  const progressionText = `Question <strong>${getCurrentIndex()+1}</strong> of <strong>${programming_exercises.length}</strong>`;
  document.getElementById("challenge_progression_text").innerHTML = progressionText;

  // Add testing examples info to the requirements block (temporary)
  const static_requirement_info = "Your program should display the outputs in the table (shown on the right) for the given inputs provided.";
  $("#requirement + p").append(`</br></br> <p>${static_requirement_info}</p>`);
  
  // Hides the next/prev challenge buttons if there is no challenge available in that direction.
  const index = getCurrentIndex();
  if (index === programming_exercises.length-1) {
    $("#next_challenge_button").find('button').hide()
  } else if (index === 0) {
    $("#prev_challenge_button").find('button').hide()
  }
}

exports.setupLessonNav = setupLessonNav;
exports.getPreviousChallengeURL = getPreviousChallengeURL;
exports.getNextChallengeURL = getNextChallengeURL;
