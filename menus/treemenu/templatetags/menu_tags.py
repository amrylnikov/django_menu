from django import template
from menus.treemenu.models import Menu

register = template.Library()
app_name = 'treemenu'


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.get(name=menu_name)
    request = context['request']
    return render_menu(menu, request.path)


def render_menu(menu, path):
    output = '<ul>'
    for item in menu.children.all():
        is_active = path.startswith(item.url)
        output += f'''
        <li class="{"active" if is_active else ""}">
        <a href="{item.url}">{item.name}</a>
        '''
        if item.children.exists():
            output += render_menu(item, path)
        output += '</li>'
    output += '</ul>'
    return output
