/** JavaScript to load on each page of website */
$(document).ready(function() {
  $("#content-container, #glossary-modal").on("click", ".glossary-term", open_glossary_definition);
});

function open_glossary_definition() {
  /**
   * Retrieve glossary definition.
   */
  var slug = $(this).data("glossary-term");
  var glossary_modal = $("#glossary-modal");

  if (glossary_modal.attr("data-glossary-term") == slug) {
    glossary_modal.modal('show');
  } else {
    // TODO: Allow URL to work for different languages
    var url = "/topics/glossary/";
    $.ajax({
      type: "GET",
      url: url,
      data: "term=" + slug,
      async: true,
      cache: true,
      dataType: "json",
      success: update_glossary_modal
    });
  }
}

function update_glossary_modal(data) {
  /**
   * Update the glossary modal with definition data.
   * @param {dict} data - The JSON data for the definition.
   */
  var glossary_modal = $("#glossary-modal");
  glossary_modal.attr("data-glossary-term", data.slug);
  $("#glossary-modal-term").text(data.term);
  $("#glossary-modal-definition").html(data.definition);
  if (!glossary_modal.hasClass('show')) {
    glossary_modal.modal('show');
  }
}
