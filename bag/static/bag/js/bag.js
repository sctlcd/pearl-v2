$('document').ready(function($) {

  // Update quantity on click
  $('.update-link').click(function(e) {
    var form = $(this).parent().prev('.update-form');
    form.submit();
  })
});
