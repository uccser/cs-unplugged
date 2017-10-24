$(document).ready(function() {
  $("form#resource-generation-form :input").on("change",  updateResourceThumbnail);
  updateResourceThumbnail();
});

function updateResourceThumbnail() {
  /**
   * Update resource thumbnail with currently selected options.
   */
  var form = $("form#resource-generation-form");
  var thumbnail_filename = form.attr("data-resource-slug") + "-";
  var values = form.serializeArray();
  values.sort(sortValuesAlphabetically);
  var query_string = "";
  values.forEach(function(value){
    if (["header_text", "copies"].indexOf(value.name) === -1) {
      query_string += value.name + "-" + value.value + "-";
    }
  });
  query_string = query_string.slice(0, -1);
  thumbnail_filename += query_string + ".png";
  var thumbnail = document.getElementById("resource-thumbnail");
  thumbnail.src = thumbnail.getAttribute("data-resource-thumbnail-base") + thumbnail_filename;
}

function sortValuesAlphabetically(a, b){
  return ((a.name < b.name) ? -1 : ((a.name > b.name) ? 1 : 0));
}
