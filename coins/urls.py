"""coins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views_login
from cartao_credito import urls as cartao_credito_urls
from despesas import urls as despesas_urls
from receitas import urls as receitas_urls
from core import urls as core_urls

from .views import sigin, logout_now

urlpatterns = [
    path('', include(core_urls), name='home'),
    path('login/', views_login.LoginView.as_view(), name='login'),
    path('logout/', logout_now, name='logout'),
    path('sigin/', sigin, name='sigin'),
    path('cartao-credito/', include(cartao_credito_urls), name='cartao-credito'),
    path('despesas', include(despesas_urls), name='despesas'),
    path('receitas', include(receitas_urls), name='receitas'),
    path('admin/', admin.site.urls),
]
