from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=100)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name}: $ {self.price} : quantity {self.quantity}'
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
        }

class UserProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="products")
    count = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user}: {self.product.name} :{self.count}'
    def to_json(self):
        return{
            'id':self.id,
            'user':self.user,
            'product':self.product,
            'count':self.count
        }

