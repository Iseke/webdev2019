from api.models import Product,UserProduct
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from api.serializers import ProductSerializer,UserProductSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.filters import ProductFilter
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductList(APIView):
    def get(self,request):
        task_lists = Product.objects.all()
        serializer = ProductSerializer(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # TODO DjangoFilterBackend
    filter_class = ProductFilter
    filterset_fields = ('name', 'price')
class UserProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProductSerializer
    def get_queryset(self):
        return UserProduct.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        product = Product.objects.get(id=self.request.data['product']['id'])
        product.quantity = product.quantity - self.request.data['count']
        product.save()
        serializer.save(user=self.request.user)

class DeleteProduct(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class =  UserProductSerializer

    def perform_destroy(self, instance):
        product = Product.objects.get(id = instance.product.id)
        product.quantity = product.quantity - instance.count
        product.save()
        instance.delete()
    def get_queryset(self):
        try:
            user_product = UserProduct.objects.get(id=self.kwargs.get('pk'))
        except UserProduct.DoesNotExist:
            raise Http404
        quaryset = user_product.products.all()
        return quaryset