from django.shortcuts import render, redirect
from .models import Product
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def intro(request):
    return render(request, 'products/intro.html')
    
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
    body = request.POST['body']
    
    image = None
    if 'image' in request.FILES:
        image = request.FILES['image']
    
    product = Product(user=user, body=body, image=image, created_at=timezone.now())
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