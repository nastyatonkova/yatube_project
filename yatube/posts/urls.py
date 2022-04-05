# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('', views.index),
    # page with the group list
    path('group/', views.group_list),
    # page for a certain group
    path('group/<slug:slug>/', views.group_posts)
]
