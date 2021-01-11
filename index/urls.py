from django.contrib import admin
from django.urls import path, include, re_path
# from index.views import index
from index import views



urlpatterns = [
    # re_path(r'^$', index, name = 'index_page'),
    path('index/', views.index.as_view(), name = 'index_person_detail'),


]