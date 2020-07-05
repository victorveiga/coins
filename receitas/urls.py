from django.urls import path

from .views import receitas, receitas_create, receitas_update

urlpatterns = [
    path('/list', receitas, name='receitas'),
    path('/new', receitas_create, name='new'),
    path('/update/<int:id>', receitas_update, name='update'),
]
