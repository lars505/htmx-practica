from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def check_product(request):
    product = request.GET.get("product")

    products = Product.objects.filter(name=product)
    
    return render(request,"partials/htmx_components/check_products.html",{'products':products})
 
def save_product(request):
    name = request.POST.get("product")
    price = request.POST.get("price")

    product = Product(
        name = name, 
        price = price 
    )

    product.save()
    products = Product.objects.all()

    return render(request,"partials/htmx_components/list_all_products.html",{'products':products})