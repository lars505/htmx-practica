from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def check_product(request):
    product = request.GET.get("product")

    products = Product.objects.filter(name=product)
    
    return render(request,"partials/htmx_components/check_products.html",{'products':products})


def validate_price(request):
    precio = request.GET.get('price')

    return render(request, "partials/htmx_components/validate_price.html",{'price':precio.isnumeric()})
 
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

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_product(request, id_product):
    product = get_object_or_404(Product, pk = id_product)

    product.delete()

    return render(request, "partials/htmx_components/list_all_products.html",{'products':Product.objects.all()})