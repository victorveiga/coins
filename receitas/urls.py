from django.urls import path

from .views import receitas, receitas_create

urlpatterns = [
    path('/list', receitas, name='receitas'),
    path('/new', receitas_create, name='new'),
]
