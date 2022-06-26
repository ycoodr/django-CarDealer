from django import template
 
register = template.Library()
 
from ..models import Car
 
@register.simple_tag
def total_events():
    return Car.objects.count()
