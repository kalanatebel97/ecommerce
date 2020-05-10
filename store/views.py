from django.contrib.auth.forms import UserCreationForm
from django.http import response
from django.shortcuts import render, redirect
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import Product,Category,Cart,CartItem
from .serializers import ProductSerializer,CategorySerializer,CartItemSerializer,CartSerializer
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

def category(request):
    context = {}
    return render(request,'store/category.html',context)

def productDetails(request):
    context = {}
    return render(request,'store/single-product.html',context)

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
         form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(response,'store/register.html',{"form": form})

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductLimitPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name','description','category_id__title')
    ordering_fields  = ('name','description','category_id__title')

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryLimitPagination

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