# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # page with the group list
    path('posts/', views.group_list, name='group_list'),
    # page for a certain group
    path('group/<slug:slug>/', views.group_posts, name='group_posts')
]
