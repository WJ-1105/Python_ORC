from django.contrib import admin
from django.urls import path, include, re_path
from index.views import index

urlpatterns = [
    re_path(r'^$', index, name = 'index_page'),
]