from django.shortcuts import render
from products.models import Product
from products.serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

# @api_view(['GET'])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# temp 



def create_superuser(request):

    username = "SuperUser1"
    email = "superuser.com"
    password = "SuperUser@123456789"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        return HttpResponse("Superuser created successfully")

    return HttpResponse("Superuser already exists")