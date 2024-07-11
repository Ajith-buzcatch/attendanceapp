from django import template
from django.urls import resolve, reverse, NoReverseMatch
from master.models import EmployeeDesignation
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_designation(employee_id):
    if employee_id:
        return EmployeeDesignation.objects.filter(employee=employee_id).first().designation.designation
    return ''

# @register.simple_tag
# def active(request, pattern):
#     url_name =resolve(request.path).url_name
#     return 'active' if url_name == pattern else ''

@register.simple_tag(takes_context=True)
def active(context, *urls):
    request = context['request']
    for url in urls:
        try:
            if request.path == reverse(url):
                return 'active'
        except NoReverseMatch:
            continue
    return ''
