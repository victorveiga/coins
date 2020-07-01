from django.urls import path, include

from .views import despesas

urlpatterns = [
    path('', despesas, name='despesas'),
]   
