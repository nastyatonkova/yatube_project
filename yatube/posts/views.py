# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import os

#  'posts/index.html' for MAC and 'posts-index.html' for WIN
PATH_TO_INDEX = os.path.join('posts', 'index.html')
PATH_TO_GROUP_LIST = os.path.join('posts', 'group_list.html')


def index(request):
    template = PATH_TO_INDEX
    title_dict = 'Main page for project Yatube'
    # Dictionary
    context = {
        'title_dict': title_dict
    }
    return render(request, template, context)


def group_list(request):
    template = PATH_TO_GROUP_LIST
    title_dict = 'Information about groups of project Yatube'
    # Dictionary
    context = {
        'title_dict': title_dict
    }
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Group number {slug}')
