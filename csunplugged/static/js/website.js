$(document).ready(function() {
  $("#content-container, #glossary-modal").on("click", ".glossary-term", open_glossary_definition);
});

// Retrieve glossary definition
function open_glossary_definition() {
  // Save glossary slug
  var slug = $(this).data("glossary-term");
  // Find glossary modal
  var glossary_modal = $("#glossary-modal");

  // If glossary modal already has content for term
  if (glossary_modal.attr("data-glossary-term") == slug) {
    glossary_modal.modal('show');
  }
  // Otherwise download HTML of modal and add to DOM
  else {
    var url = "/topics/glossary/" + slug
    $.ajax({
      type: "GET",
      url: url,
      async: true,
      cache: true,
      dataType: "json",
      success: update_glossary_modal
    });
  }
}

// Update the glossary modal with definition data
function update_glossary_modal(data) {
  var glossary_modal = $("#glossary-modal");
  glossary_modal.attr("data-glossary-term", data["slug"]);
  $("#glossary-modal-term").text(data["term"]);
  $("#glossary-modal-definition").html(data["definition"]);
  if (!glossary_modal.hasClass('show')) {
    glossary_modal.modal('show');
  }
}
