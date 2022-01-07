from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer2

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer2

'''
viewsets & router
this makes it really easy to navigate our models, with just the single view above
we could do alot of things get all product list, a single product detail, update a product, delete a product
the router add a lot of url params eg below, which we can query to get these functionality
api/v2/ ^products-xyz\.(?P<format>[a-z0-9]+)/?$ [name='products-list']
api/v2/ ^products-xyz/(?P<pk>[^/.]+)/$ [name='products-detail']
api/v2/ ^products-xyz/(?P<pk>[^/.]+)\.(?P

'''