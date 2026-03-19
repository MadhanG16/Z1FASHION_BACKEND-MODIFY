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



from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

def create_admin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return HttpResponse("Username and password required!", status=400)

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!", status=400)

        User.objects.create_superuser(
            username=username,
            password=password
        )

        return HttpResponse("Superuser created successfully!")

    return HttpResponse("Invalid request method!", status=405)