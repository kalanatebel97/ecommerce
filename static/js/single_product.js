$(document).ready(function () {

    $.ajax({

       type : 'GET',
       url  : 'http://127.0.0.1:8000/api/products/?search=shoes',
        datatype : 'json',
        success: function (data) {
                console.log(data)
        }

    });

});
