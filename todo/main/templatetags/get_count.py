from django.template.defaulttags import register
from todo.settings import MAXLEN


@register.filter()
def get_count(list_temp):
    if len(list_temp) < MAXLEN:
        return range(MAXLEN-len(list_temp))
