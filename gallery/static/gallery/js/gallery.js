$('document').ready(function($) {

  // Gallery filters
  $('.gallery-filters li').on('click', function() {
    $('.gallery-filters li').removeClass('active');
    $(this).addClass('active');
    filter = $(this).attr('gallery-filter');

    $('.gallery-img-holder').each(function() {
      if (filter == 'all') {
        $(this).fadeIn();
      } else {
        $(this).hide();
        if ($(this).attr('filter-category') == filter) {
          $(this).fadeIn();
        }
      }
    });
  });

});
