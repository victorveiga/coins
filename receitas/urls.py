from django.urls import path

from .views import receitas

urlpatterns = [
    path('/list', receitas, name='receitas'),
]
