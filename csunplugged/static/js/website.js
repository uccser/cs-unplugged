/** JavaScript to load on each page of website */
$(document).ready(function() {
  $("#content-container, #glossary-modal").on("click", ".glossary-term", open_glossary_definition);
});

function open_glossary_definition() {
  /**
   * Retrieve glossary definition.
   */
  var glossary_modal = $("#glossary-modal");
  if (!glossary_modal.hasClass('show')) {
    glossary_modal.modal('show');
  }

  var slug = $(this).data("glossary-term");
  if (glossary_modal.attr("data-glossary-term") != slug) {
    // TODO: Allow code to work for different languages
    $("#glossary-modal-term").text("Loading glossary definition...");
    $("#glossary-modal-definition").html("");
    var url = "/topics/glossary/json/";
    $.ajax({
      type: "GET",
      url: url,
      data: "term=" + slug,
      async: true,
      cache: true,
      dataType: "json",
      success: update_glossary_modal,
      error: show_glossary_modal_error,
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
}

function show_glossary_modal_error(jqXHR, text_status, error_thrown) {
  /**
   * Update the glossary modal with an error.
   * @param {jqXHR} jqXHR - The jqXHR object.
   * @param {str} text_status - Describes the type of error that occurred.
   * @param {str} error_thrown - Optional exception object, if one occurred.
   */
  var glossary_modal = $("#glossary-modal");
  glossary_modal.attr("data-glossary-term", "");
  $("#glossary-modal-term").text("Error!");
}
