$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/dog_aid/suggest/', {suggestion: query}, function(data){
        $('#illness_suggest').html(data);
    });
});

$('#emergency_suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/dog_aid/emergency_suggest/', {emergency_suggestion: query}, function(data){
        $('#emergency_suggest').html(data);
    });
});