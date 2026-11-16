from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from . import models, serializers

# Create your views here.


class ProductsAPI(APIView):
    def get(self, request: Request):
        data = models.Product.objects.select_related("category").all()
        serialized_data = serializers.ProductSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


