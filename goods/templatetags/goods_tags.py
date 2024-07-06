from urllib.parse import urlencode
from django import template
from typing import Any

from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs) -> str:
    # Kopiera GET-parametrarna från request-objektet
    query: dict[str, Any] = context['request'].GET.copy()
    # Uppdatera query dict med de nya parametrarna
    query.update(kwargs)
    # Returnera den uppdaterade query-strängen
    return urlencode(query)
