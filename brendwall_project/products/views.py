from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from django.shortcuts import render


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request):
    return render(request, 'index.html')
