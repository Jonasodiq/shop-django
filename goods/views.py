from django.db.models import Manager
from django.shortcuts import render

import goods
from goods.models import Products

def catalog(request):

    goods: Manager(Products) = Products.objects.all()

    context: dict[str, Any] = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, "goods/catalog.html", context)

def product(request):
    return render(request, "goods/product.html")
