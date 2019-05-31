from rest_framework import serializers
from api.models import Product,UserProduct
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('id','username','email')


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=False)
    class Meta:
        model=Product
        fields = ('id','name','price','quantity')
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class UserProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    product = ProductSerializer(many=True)
    count = serializers.IntegerField(read_only=True)
    class Meta:
        model=UserProduct
        fields = ('id','user','product','count')


