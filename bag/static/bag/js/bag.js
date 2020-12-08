$('document').ready(function($) {
  
  // Go to the top of the page
  $('.btt-button-top').click(function(e) {
    window.scrollTo(0, 0)
  })

  // Go to the bottom of the page
  $('.btt-button-down').click(function(e) {
    window.scrollTo(0, document.body.scrollHeight)
  })

  // Update quantity on click
  $('.update-link').click(function(e) {
    var form = $(this).parent().prev('.update-form');
    form.submit();
  })
};
