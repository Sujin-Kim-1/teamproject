from django.shortcuts import render, redirect
from .models import Product
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def intro(request):
    return render(request, 'products/intro.html')

@login_required    
def index(request):

    product = Product.objects.all()
    context = { 'product': product }
    return render(request, 'products/menumain.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = { 'product': product }
    return render(request, 'products/detail.html', context)

@login_required
def new(request):
    return render(request, 'products/new.html')

@login_required
def create(request):
    user = request.user
    comment = request.POST['comment']
    brand = request.POST['brand']
    productname = request.POST['productname']
    price = request.POST['price']
    site = request.POST['site']


    producttype = request.POST['producttype']
    category_m = request.POST['category_m']
    style_m = request.POST['style_m']
    color = request.POST['color']
    season = request.POST['season']
    rating = request.POST['rating']

    
    image = None
    if 'image' in request.FILES:
        image = request.FILES['image']
    
    product = Product(user=user, category_m=category_m, comment=comment, brand=brand, productname=productname, price=price, site=site, image=image, producttype=producttype, style_m=style_m, color=color, season=season, rating=rating, created_at=timezone.now())
    product.save()
    return redirect('products:detail', product_id=product.id)

@login_required
def edit(request, product_id):
    try:
        product = Product.objects.get(id=product_id, user=request.user)
    except Product.DoesNotExist:
        return redirect('products:menumain')

    context = { 'product': product }
    return render(request, 'products/edit.html', context)

@login_required
def update(request, product_id):
    try:
        product = Product.objects.get(id=product_id, user=request.user)
    except Product.DoesNotExist:
        return redirect('products:menumain')

    product.body = request.POST['body']
    
    if 'image' in request.FILES:
        product.image = request.FILES['image']
        
    product.save()
    return redirect('products:detail', product_id=product.id)

@login_required
def delete(request, product_id):
    try: 
        product = Product.objects.get(id=product_id, user=request.user)
    except Product.DoesNotExist:
        return redirect('products:menumain')

    product.delete()
    return redirect('products:menumain')