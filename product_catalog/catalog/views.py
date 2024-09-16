# catalog/views.py

from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.db.models import F
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category']

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        data = request.data
        if 'sales' in data:
            product.sales = F('sales') + data['sales']
            product.save()
            return Response(self.get_serializer(product).data)
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for product in queryset:
            product.popularity = product.sales
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
