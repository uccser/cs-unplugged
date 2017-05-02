$(document).ready(function(){
  $("#content-container").on("click", ".glossary-term", function() {
    // Get glossary slug
    var slug = $(this).data("glossary-term")
    var glossary_term_container = $("#glossary-terms")

    // Find existing modal
    var glossary_modal = glossary_term_container.children("#glossary-term-" + slug)
    if (glossary_modal.length) {
      glossary_modal.modal('show')
    }
    // Otherwise download HTML of modal and add to DOM
    else {
      var url = "/topics/glossary/" + slug
      $.ajax({
        type: "GET",
        url: url,
        async: true,
        dataType: "html",
        success: function (glossary_html) {
          var glossary_modal = $(glossary_html);
          $("#glossary-terms").append(glossary_modal);
          glossary_modal.modal('show');
        }
      });
    }
  });
});
