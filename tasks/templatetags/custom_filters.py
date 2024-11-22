from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Adiciona classes CSS aos campos do formulário"""
    return field.as_widget(attrs={"class": css_class})
