from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context: dict[str, str] = {
        'title': 'Home - Startsida',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Home - Om oss',
        'content': 'Om oss',
        'text_on_page': "Text om varför vi är bäst och varför ska du välja oss"
    }

    return render(request, 'main/about.html', context)


