from django.template import Library

register = Library()

@register.filter
def trunc(text, count=1):
    text = text.split(".")[count]
    return text + "..."