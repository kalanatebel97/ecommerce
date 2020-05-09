from django.contrib.auth.forms import UserCreationForm
from django.http import response
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

from .models import Product,Category

from .serializers import ProductSerializer,CategorySerializer


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

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
