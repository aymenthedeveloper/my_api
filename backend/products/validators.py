from .models import Product
from rest_framework import serializers


def validate_title(value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("title already exists! a product title must be unique")
        return value


