from django import template
register = template.Library()
from ..views import subscribers


def check_subscriber(sub):
    for subscriber in subscribers:
        if subscriber==sub:
            return True
    return False