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

  $('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
	});

});
