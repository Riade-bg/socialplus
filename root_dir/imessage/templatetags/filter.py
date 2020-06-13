from django import template
register = template.Library()

@register.filter(name='hash')
def hash(h, key):
    for i in range(len(h)):
        if key == h[i]['reciever_id']:
            return h[i]['message']