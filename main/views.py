# from django.db.models import BaseManager
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from goods.models import Categories

def index(request):

    categories: BaseManager[Categories] = Categories.objects.all()

    context: dict[str, Any] = {
        'title': 'Home - Startsida',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)


