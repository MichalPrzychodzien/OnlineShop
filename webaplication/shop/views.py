from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Product, Producent

def index(request):
    products_list = Product.objects.all()
    context = {
        'p_list' : products_list
    }

    return render(request, 'shop/index.html', context)

