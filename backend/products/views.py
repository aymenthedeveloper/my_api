from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

    def perform_update(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        print(serializer.validated_data)
        if content is not None:
            content = title
        serializer.save(content=content)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        print(serializer.validated_data)
        if content is not None:
            content = title
        serializer.save(content=content)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        print(serializer.validated_data)
        if content is not None:
            content = title
        serializer.save(content=content)

