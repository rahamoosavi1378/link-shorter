"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('r/', views.redirect_page),
    path('r/<str:hash_redirect>', views.redirect_hash, name='hash_redirect'),
    path('h/<str:hash_r_10_char>', views.redirect_hash_10_char,
         name='hash_r_10_char'),
    path('s/<slug:hash_r_slug>', views.redirect_hash_slug, name='hash_r_slug'),
]
