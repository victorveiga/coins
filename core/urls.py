from django.urls import path, include

from .views import home
from receitas import urls as receitas_urls
from cartao_credito import urls as cartao_credito_urls
from despesas import urls as despesas_urls

urlpatterns = [
    path('', home, name='home'),
    path('receitas', include(receitas_urls), name='receitas'),
    path('cartao-credito/', include(cartao_credito_urls), name='cartao-credito'),
    path('despesas', include(despesas_urls), name='despesas'),
]
