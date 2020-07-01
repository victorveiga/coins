from django.urls import path

from .views import cartao_credito

urlpatterns = [
    path('', cartao_credito,name='cartao-credito')
]
