/* If within top 50px pixels of page, navbar becomes transparent */
$(window).scroll(function() {
  if($(this).scrollTop() > 50) {
      $('.navbar').removeClass('trans-navbar');
  } else {
      $('.navbar').addClass('trans-navbar');
  }
});
