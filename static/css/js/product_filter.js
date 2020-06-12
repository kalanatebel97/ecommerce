$(document).ready(function () {

    let productListEl = $('#product-list');
    let singleProductEl = $('#single-product-template');
    singleProductEl.hide();
    productFilter("shoes");
    $('.categoryTitle').on("click",function () {
        var categoryTitle = $(this).data('category');
        console.log(categoryTitle);
        productFilter(categoryTitle);
    })

});



function productFilter(categoryTitle){

    var apiUrl = 'http://127.0.0.1:8000/api/products/?category=true&search=';
    var url = apiUrl += categoryTitle;
    let productListEl = $('#product-list');
    let singleProductEl = $('#single-product-template');
    // var filterUrl = 'http://127.0.0.1:8000/api/products/?category=true&search=';
    $.ajax({
        type: 'GET',
        url: url,
        datatype: 'json',
        success: function (data) {
            productListEl.empty();
            let products = data.results;
            $.each(products, function (index, product) {
                singleProductEl.find('h6.single-product-name').text(product.name);
                singleProductEl.find('h6.single-product-price').text(product.price);
                // singleProductEl.find('#viewMore').text(product.id);
                // singleProductEl.find('').text(product.id);
                $("#social-info").attr("href",'/single-product/'+product.id)
                productListEl.append(singleProductEl.html());
            });

        }
    });
}







