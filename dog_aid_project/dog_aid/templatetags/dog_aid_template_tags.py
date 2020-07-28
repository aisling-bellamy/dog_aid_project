from django import template
from dog_aid.models import Category

register=template.Library()
@register.inclusion_tag('dog_aid/categories.html')
def get_category_list():
    return {'categories': Category.objects.all()}