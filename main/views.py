from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Home pege',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
