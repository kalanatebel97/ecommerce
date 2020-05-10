from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet, )
router.register(r'api/categories', views.CategoryViewSet, )
router.register(r'api/cart', views.CartViewSet, )
router.register(r'api/cartItems', views.CartItemViewSet, )

urlpatterns = [
    path('index/',views.index , name = "index"),
    # path('store/',views.store , name = "store"),
    # path('cart/',views.cart , name = "cart"),
    # path('checkout/',views.checkout , name = "checkout"),
    # path('login/',views.login , name = "login"),
    # path('category/',views.category , name = "category"),
    # path('single-product/',views.productDetails , name = "productDetails"),
    # path('cart/',views.cart , name = "cart"),
    # path('/products', ProductViewSet(), name ="products"),
    path('register/', views.register, name="register"),
    # path('login/', views.login, name="login"),
    path('',include('django.contrib.auth.urls')),
    path('', include(router.urls)),

]
