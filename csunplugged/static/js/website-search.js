$(document).ready(function() {
  $('#models-filter').multipleSelect({
    selectAll: false,
    width: '100%',
    placeholder: "Show all types",
  });

//   $('#areas-filter').multipleSelect({
//     filter: true,
//     textTemplate: formatArea,
//     labelTemplate: formatArea,
//     selectAll: false,
//     width: '100%',
//     onClick: updateSelectedAreas,
//     onOptgroupClick: updateSelectedAreas,
//     maxHeight: 500,
//   });

  // Render selected areas on initial load.
//   updateSelectedAreas();

  // Indent all area children.
//   $('.areas-filter-container .ms-drop li:not(.group)').find(':checkbox').each(function(i, obj) {
//     if (areaData[$(this).val()]['child']) {
//       $(this).addClass('area-child');
//     }
//   });

  // Clear form button.
  $('#clear-form').click(function(){
     $('#id_q').val('');
     $('#models-filter').multipleSelect('uncheckAll');
    //  $('#areas-filter').multipleSelect('uncheckAll');
    //  updateSelectedAreas();
 });
});

// function createAreaBadge(id) {
//     /**
//      * Create HTML of curriculum area badge.
//      * @param {int} id - ID for area to create badge for.
//      * @return {string} HTML of curriculum area badge.
//      */
//     var area_data = areaData[id];
//     var child_class = '';
//     if (area_data.child) {
//         child_class = ' area-child';
//     }
//     return `<span class="area-badge badge-${area_data.colour}${child_class}">${area_data.text}</span>`;
// };

// function updateSelectedAreas(changeData) {
//   /**
//    * Update selected field with curriculum area badges.
//    * @param {object} changeData - Data of the clicked item.
//    */
//   var $selectedSpan = $('.areas-filter-container .ms-choice span');
//   $selectedSpan.empty();
//   var $selectedValues = $('#areas-filter').multipleSelect('getSelects');
//   if ($selectedValues.length == 0) {
//     $selectedSpan.text("Show all curriculum areas");
//   } else {
//     for (var i = 0; i < $selectedValues.length; i++) {
//       $selectedSpan.append(createAreaBadge($selectedValues[i]));
//     }
//   }
// };

// function formatArea(element) {
//     /**
//      * Render curriculum area option in multiple select widget.
//      * @param {Node} element - Element to render text.
//      * @return {string} HTML of curriculum area badge.
//      */
//     var element_value = element[0].value;
//     if (!element_value) {
//         element_value = element[0].dataset.value;
//     }
//     return createAreaBadge(element_value);
// };
