from django.contrib.auth.forms import UserCreationForm
from django.http import response, request
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import login, authenticate

from .ProductFilter import ProductSearchFilter
from .forms import RegisterForm
from .models import Product, Category, Cart, CartItem, SubCategory,CustomUser
from .serializers import ProductSerializer, CategorySerializer, CartItemSerializer, CartSerializer, \
    SubCategorySerializer
from .pagination import CategoryLimitPagination,CategoryPageNumberPagination,ProductLimitPagination,ProductPageNumberPagination

def index(request):
    context = {}
    return render(request,'store/index.html',context)

def login(request):
    context = {}
    return render(request,'store/login.html',context)

def store(request):
    context = {}
    return render(request,'store/store.html',context)

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)

# def category(request):
#     context = {}
#     return render(request,'store/products.html',context)
def comingsoon(response):
    context = {}
    return render(response,'store/comingsoon.html',context)

def categoryList(request):
    category_tree = []
    categories = Category.objects.all()
    category: Category
    for category in categories:
        sub_categories = category.subcategory_set.all()
        category_tree_item = {"id": category.id, "title": category.title, "sub_categories": []}
        for sub_category in sub_categories:
            category_tree_item["sub_categories"].append({
                "id": sub_category.id,
                "title": sub_category.title,
            })
        category_tree.append(category_tree_item)
    return render(request,'store/products.html',{'categories': category_tree})

def productDetails(request,product_id):
    product = Product.objects.get(pk= product_id)
    categoryTitle = product.category_id.title

    return render(request,'store/single-product.html',{'product': product,'category' : categoryTitle})

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
              form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(response,'store/register.html',{"form": form})

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductLimitPagination
    filter_backends = (ProductSearchFilter,OrderingFilter)
    ordering_fields  = ('name','description','category_id__title')

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryLimitPagination

class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=False, methods=['GET'], url_path='my-cart')
    def get_my_cart(self, request, *args, **kwargs):
        queryset = Cart.objects.filter(user=request.user).first()

        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)

class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.get(pk=request.data['productId'])
        # productPrice = Product.objects.get(pk=request.data['total_price'])
        productPrice = request.data['totalPrice']
        quantity = int(request.data['quantity'])
        # print(request.data['productId'],request.data['quantity']);
        totalPrice = productPrice * quantity;
        cartItem = CartItem(product=product, quantity=quantity, cart=cart,total_price = totalPrice)
        cartItem.save()
        serializer = self.get_serializer(cartItem, many=False)
        return Response(serializer.data)








