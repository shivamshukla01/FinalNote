$(document).ready(function() {
  
  $(window).scroll(function () {
      //if you hard code, then use console
      //.log to determine when you want the 
      //nav bar to stick.  
      console.log($(window).scrollTop())
    if ($(window).scrollTop() > 63) {
      $('.navbar').addClass('navbar-fixed-top');
      $('.navbar-brand').removeClass('navbar-brand-hidden');
    }
    if ($(window).scrollTop() <0.1 ) {
      $('.navbar').removeClass('navbar-fixed-top');
      $('.navbar-brand').addClass('navbar-brand-hidden');

    }
  });
});

  // Add slideDown animation to Bootstrap dropdown when expanding.
  $('.dropdown').on('show.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // Add slideUp animation to Bootstrap dropdown when collapsing.
  $('.dropdown').on('hide.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
  });