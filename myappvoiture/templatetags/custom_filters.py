from django import template

register = template.Library()

@register.filter
def masked_password(password):
    """
    Returns a masked password with asterisks.
    """
    return '*' * len(password)
