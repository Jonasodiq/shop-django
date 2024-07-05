# from django.core.paginator import Paginator
# from django.db.models import Manager
# from django.shortcuts import get_list_or_404, render

# from goods.models import Products
# from typing import Any

# def catalog(request, category_slug, page=1):

#     if category_slug == 'all':
#         goods: Manager(Products) = Products.objects.all()
#     else:
#         goods: Any = get_list_or_404(Products.objects.filter(category__slug=category_slug))

#     paginator = Paginator(goods, 3)
#     current_page: Page = paginator.page(page)

#     context: dict[str, Any] = {
#         'title': 'Home - Каталог',
#         'goods': current_page,
#         'slug_url': category_slug,
#     }
#     return render(request, "goods/catalog.html", context)

# def product(request, product_slug):

#     product: Products = Products.objects.get(slug = product_slug)

#     context: dict[str, Products] = {
#         'product': product
#     }

#     return render(request, "goods/product.html", context=context)


#######

from django.core.paginator import Paginator, Page
from django.db.models import Manager, QuerySet
from django.shortcuts import get_list_or_404, render, get_object_or_404

from goods.models import Products
from typing import Any, Dict

def catalog(request, category_slug: str, page: int = 1):

    if category_slug == 'all':
        goods: QuerySet[Products] = Products.objects.all()
    else:
        goods: QuerySet[Products] = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page: Page = paginator.page(page)

    context: Dict[str, Any] = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug: str):

    product: Products = get_object_or_404(Products, slug=product_slug)

    context: Dict[str, Products] = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)
