from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    pass


def products_list(request):
    products = Product.actives.all()
    context = {
        'products': products
    }
    return render(request, '', context)


def product_detail(request, pk):
    pass
