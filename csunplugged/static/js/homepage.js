$(window).scroll(function() {
  if($(this).scrollTop() > 50)  /*height in pixels when the navbar becomes transparent*/
  {
      $('.navbar').removeClass('trans-navbar');
  } else {
      $('.navbar').addClass('trans-navbar');
  }
});
