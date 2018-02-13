$(window).scroll(function() {
  if($(this).scrollTop() > 50)  /*height in pixels when the navbar becomes transparent*/
  {
      $('.trans-navbar').removeClass('trans');
  } else {
      $('.trans-navbar').addClass('trans');
  }
});
