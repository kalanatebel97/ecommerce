$(document).ready(function () {
 var apiUrl = 'http://127.0.0.1:8000/api/products/?search=';
    var productId = $(this).data('product');
    console.log(productId);
    var url = apiUrl += productId;
    let productListEl = $('#product-list');
    let singleProductEl = $('#single-product-template');
    $.ajax({

       type : 'GET',
       url  : apiUrl,
        datatype : 'json',
        success: function (data) {
            productListEl.empty();
            // var product = JSON.parse(data.results);
            console.log(data.results);
            singleProductEl.find('h3.s_product_text').text(product.name);
            singleProductEl.find('h2.s_product_text').text(product.price);
            productListEl.append(singleProductEl.html());
            // $.each(products, function (index, product) {
            //     singleProductEl.find('h3.s_product_text').text(product.name);
            //     singleProductEl.find('h2.s_product_text').text(product.price);
            //     productListEl.append(singleProductEl.html());
            // });

        }

    });

});
