from django.urls import path
from django.contrib import admin
from menus.treemenu.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('<str:menu_name>/', IndexView.as_view(), name='menu_link'),
]
