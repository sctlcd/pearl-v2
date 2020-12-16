$('document').ready(function($) {

  $('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal != "reset") {
      var sort = selectedVal.split("_")[0];
      var direction = selectedVal.split("_")[1];

      currentUrl.searchParams.set("sort", sort);
      currentUrl.searchParams.set("direction", direction);

      window.location.replace(currentUrl);
    } else {
      currentUrl.searchParams.delete("sort");
      currentUrl.searchParams.delete("direction");

      window.location.replace(currentUrl);
    }
  });

	// Trigger the click event on the delete-product-link id element
  $('#delete-product-link').click(function(event) {
		$('.delete-modal').modal('show');
	});

	// Trigger the click event on the edit-product-link id element
	$('#edit-product-link').click(function(event) {
		$('.edit-modal').modal('show');
	});

	$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
	});
});
