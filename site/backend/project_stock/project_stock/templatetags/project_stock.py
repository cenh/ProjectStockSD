from django.core.validators import EmailValidator, URLValidator
from django import template

register = template.Library()

@register.simple_tag
@stringfilter
def validate_email(email):
    validator = EmailValidator()
    if validator.regex.match(email):
        return False
    else:
        return email

@register.simple_tag
@stringfilter
def validate_url(url):
    validator = URLValidator()
    if validator.regex.match(url):
        return False
    else:
        return url
