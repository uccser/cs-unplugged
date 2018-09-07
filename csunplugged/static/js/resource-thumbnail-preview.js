$(document).ready(function() {
  $("form#resource-generation-form :input").on("change",  updateResourceThumbnail);
  updateResourceThumbnail();
});

function updateResourceThumbnail() {
  /**
   * Update resource thumbnail with currently selected options.
   */
  var values = $("#resource-options :checked");
  values.sort(sortValuesAlphabetically);
  var query_string = "";
  for (var i = 0; i < values.length; i++) {
    query_string += values[i].name + "-" + values[i].value + "-";
  }
  query_string = query_string.slice(0, -1);
  var thumbnail_filename = resource_slug + "-" + query_string + ".png";
  var thumbnail = document.getElementById("resource-thumbnail");
  thumbnail.src = resource_thumbnail_base + thumbnail_filename;
}

function sortValuesAlphabetically(a, b){
  return ((a.name < b.name) ? -1 : ((a.name > b.name) ? 1 : 0));
}
