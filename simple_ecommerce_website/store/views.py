from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    context={}
    return render(request,'user/home.html',context)


def store(request):
    products=Product.objects.all();
    context={"products":products}
    return render(request,'user/store.html',context)

def cart(request):
    context={}
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        context={"items":items,"order":order}
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        context={"items":items,'order':order}

    
    return render(request,'user/cart.html',context)

def checkout(request):
    context={}
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        context={"items":items,"order":order}
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        context={"items":items,'order':order}
    return render(request,'user/checkout.html',context)
