# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# Third-party imports (DRF)
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Local app imports
from products.models import Product
from products.serializer import ProductSerializer

# Create your views here.

# @api_view(['GET'])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# temp view for creating superuser
User = get_user_model()

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def create_admin(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    User.objects.create_superuser(
        username=username,
        password=password
    )

    return Response({"message": "Superuser created successfully"})

    # test