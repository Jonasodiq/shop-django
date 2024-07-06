from django.core.paginator import Paginator, Page
from django.db.models import QuerySet
from django.shortcuts import get_list_or_404, render, get_object_or_404

from goods.models import Products
from typing import Any, Dict

from goods.utils import q_search

def catalog(request, category_slug=None):

    page: int = int(request.GET.get('page', 1))
    on_sale: str = request.GET.get('on_sale', None)
    order_by: str = request.GET.get('order_by', None)
    query: str = request.GET.get('q', None)

    if category_slug == 'all':
        goods: QuerySet[Products] = Products.objects.all()
    elif query:
        goods: QuerySet[Products] = q_search(query)
    else:
        goods: QuerySet[Products] = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
    
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

#######

# from django.core.paginator import Paginator
# from django.db.models import BaseManager, Manager
# from django.shortcuts import get_list_or_404, render

# from goods.models import Products
# from typing import Any

# def catalog(request, category_slug):

#     page: Any = request.GET.get('page', 1)
#     on_sale: Any = request.GET.get('on_sale', None)
#     order_by: Any = request.GET.get('order_by', None)

#     if category_slug == 'all':
#         goods: Manager(Products) = Products.objects.all()
#     else:
#         goods: Any = get_list_or_404(Products.objects.filter(category__slug=category_slug))

#     if on_sale:
#         goods: BaseManager[Products] | = goods.filter(discount__qt=0)

#     if order_by and order_by != "default":
#         goods: BaseManager[Products] | = goods.order_by(order_by)
    
#     paginator = Paginator(goods, 3)
#     current_page: Page = paginator.page(int(page))
 
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