from django.shortcuts import render
from django.views import View

from menus.treemenu.models import Menu


class IndexView(View):

    def get(self, request, *args, **kwargs):
        menus = Menu.objects.filter(parent=None)
        return render(request, 'menu.html', context={
            'menus': menus,
        })
