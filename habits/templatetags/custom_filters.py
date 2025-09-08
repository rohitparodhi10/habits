from django import template

register = template.Library()

@register.filter
def get_record(records, habit):
    return records.filter(habit=habit).first()