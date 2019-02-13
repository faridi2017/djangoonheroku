# djangotemplates/crm/urls.py
from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from crm import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    path('aarif/', views.AarifTest.as_view()), #faridi/aarif/
]