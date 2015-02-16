// Shorthand for $( document ).ready()
$(function() {
    console.log( "ready!" );
    $('#my-final-table').dynatable();
    console.log( "ready!" );
});

$('#my-final-table').dynatable({
  dataset: {
    records: myRecords
  }
});