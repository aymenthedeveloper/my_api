from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializers


@api_view(['POST'])
def api_home(request):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)