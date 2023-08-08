from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#customer model

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    @property
    def get_price(self):
        return self.price

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
    digital=models.BooleanField(default=False ,null=True,blank=False)

    
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping =False
        orderedItem=self.orderitem_set.all()
        for i in orderedItem:
            if i.product.digital==False:
                shipping = True
        return shipping


    @property
    def get_cart_total(self):
        orderedItem=self.orderitem_set.all()
        
        total=sum([float(item.get_total) for item in orderedItem])
        return total

    @property
    def get_cart_items(self):
        orderedItem=self.orderitem_set.all()
        total=sum([item.quantity for item in orderedItem])
        return total


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True) 
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        return (self.product.get_price * self.quantity)

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    






