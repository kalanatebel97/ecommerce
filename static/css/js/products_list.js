$(document).ready(function () {
    let productListEl = $('#product-list');
    let singleProductEl = $('#single-product-template');
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/products/',
        datatype: 'json',
        success: function (data) {
            productListEl.empty();
            let products = data.results;
            $.each(products, function (index, product) {
                singleProductEl.find('h6.single-product-name').text(product.name);
                singleProductEl.find('h6.single-product-price').text(product.price);
                productListEl.append(singleProductEl.html());
            });
        }
    });
});
