$(document).ready(function(){

$.ajax({
    type : 'GET',
    url : 'http://127.0.0.1:8000/api/categories/',
    datatype : 'json',
    success:function(data){
//        $('#mainCategories').append('<li><a>data.title<span')
          console.log(data)
    }

})

})