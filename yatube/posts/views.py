from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import os

#  'posts/index.html' for MAC and 'posts-index.html' for WIN
PATH_TEMPLATE = os.path.join('posts', 'index.html')  


def index(request):
    template = PATH_TEMPLATE
    return render(request, template)


def group_list(request):
    return HttpResponse('List of posts grouped by groups')


def group_posts(request, slug):
    return HttpResponse(f'Group number {slug}')
