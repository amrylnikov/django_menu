from django.urls import path

from menus.treemenu import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='menus_example'),
]
