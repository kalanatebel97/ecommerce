$(document).ready(function () {
    var apiUrl = 'http://127.0.0.1:8000/api/products/';
    var productId = $('#product_name').attr('data-product');
    var productCategory = $('#category-title').attr('data-cat');
    console.log(productId);
    var url = apiUrl += productId;
    let productListEl = $('#product-list');
    let singleProductEl = $('#single-product-template');
    var cartItemUrl = 'http://127.0.0.1:8000/api/cartItems/';
    // var cartItemUrl = cartUrl + '/';
    // singleProductEl.hide();


    $('#addToCart').on("click",function () {
        var quantity = $('#sst').val();
        // console.log(productId,quantity);
        addToCart(productId,quantity);

    })

    $.ajax({

       type : 'GET',
       url  : apiUrl,
        datatype : 'json',
        success: function (data) {
            productListEl.empty();
            // var product = JSON.parse(data.results);
            console.log(data);
            singleProductEl.find('h3.product-name').text(data.name);
            singleProductEl.find('h2.product-price').text(data.price);
            singleProductEl.find('#category-title').text(productCategory);
            // $("#category-title").attr("href",''+productCategory)
            singleProductEl.find('p.product-description').text(data.description);
            productListEl.append(singleProductEl.html());
        }

    });
    console.log('USER',user);

    function addToCart(productId,quantity){
        $.ajax({
            type : 'POST',
            url : cartItemUrl,
            datatype: 'json',
            headers : {'X-CSRFToken':csrftoken},
            data : {'productId' : productId,'quantity': quantity},
            success: function (data) {

            }
        });

    }

});
