$(document).ready(function () {

    var cartItemUrl = 'http://127.0.0.1:8000/api/cartItems/';
    var productElement = $('#template');

    $.ajax({
        type: 'GET',
        url : cartItemUrl,
        datatype: 'json',
        success:function (data) {
            $.each(data,function (index, product) {
                console.log(product.total_price);
                productElement.find('h5.productPrice').text(product.total_price);

            });

        }

    });




});