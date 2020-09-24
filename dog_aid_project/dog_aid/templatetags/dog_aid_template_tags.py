from django import template
from dog_aid.models import Category, Illness, Symptom

register=template.Library()

@register.inclusion_tag('dog_aid/categories.html')
def get_category_list():
    return {'categories': Category.objects.all()}

@register.inclusion_tag('dog_aid/illness_suggest.html')
def get_illness_list(illnesses=None):
    return {'illnesses': Illness.objects.all().order_by('name')}

@register.inclusion_tag('dog_aid/illness_suggest.html')
def get_symptom_list(symptoms=None):
    return {'symptoms': Symptom.objects.all().order_by('name')}

@register.inclusion_tag('dog_aid/emergency_suggest.html')
def get_emergency_list(emergency_illnesses=None):
    return {'emergency_illnesses': Illness.objects.all().order_by('name')}

@register.inclusion_tag('dog_aid/emergency_suggest.html')
def get_symptom_list(emergency_symptoms=None):
    return {'emergency_symptoms': Symptom.objects.all().order_by('name')}
