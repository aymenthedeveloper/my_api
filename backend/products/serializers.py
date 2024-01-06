from rest_framework import serializers
from.models import Product
from rest_framework.reverse import reverse
from .validators import validate_title

class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-update',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    """ def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("a product title must be unique")
        return value """

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', request=request, kwargs={'pk': obj.pk})

    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None