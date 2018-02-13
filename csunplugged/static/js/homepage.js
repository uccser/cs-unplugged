$(window).scroll(function() {
  if($(this).scrollTop() > 50)  /*height in pixels when the navbar becomes transparent*/
  {
      $('.trans-navbar').addClass('opaque');
  } else {
      $('.trans-navbar').removeClass('opaque');
  }
});
