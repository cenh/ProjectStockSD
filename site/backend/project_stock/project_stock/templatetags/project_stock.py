from django.core.validators import EmailValidator, URLValidator
from django.core.exceptions import ValidationError
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def validate_email(email):
    try:
        validator = EmailValidator()(email)
    except ValidationError:
        return False

    return email

@register.filter
@stringfilter
def validate_url(url):
    try:
        validator = URLValidator()(url)
    except ValidationError:
        return False

    return url
