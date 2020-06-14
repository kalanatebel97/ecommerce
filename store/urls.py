from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, )
router.register(r'categories', views.CategoryViewSet, )
router.register(r'cart', views.CartViewSet, )
router.register(r'cartItems', views.CartItemViewSet, )
router.register(r'subCategories', views.SubCategoryViewSet, )
# router.register(r'api/single-product', views.SingleProductViewSet, )

urlpatterns = [
    path('index/',views.index , name = "index"),
    path('', views.comingsoon, name="comingsoon"),
    # path('store/',views.store , name = "store"),
    path('cart/',views.cart , name = "cart"),
    # path('checkout/',views.checkout , name = "checkout"),
    # path('login/',views.login , name = "login"),
    path('products/',views.categoryList , name = "category"),
    path('single-product/<int:product_id>',views.productDetails , name = "productDetails"),
    # path('cart/',views.cart , name = "cart"),
    # path('/products', ProductViewSet(), name ="products"),
    path('register/', views.register, name="register"),
    # path('login/', views.login, name="login"),
    path('',include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),

]
