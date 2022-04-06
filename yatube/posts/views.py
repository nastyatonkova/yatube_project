# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('<i>Main page<i>')


def group_list(request):
    return HttpResponse('List of posts grouped by groups')


def group_posts(request, slug):
    return HttpResponse(f'Group number {slug}')
