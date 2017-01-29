# from django.shortcuts import render
#
# # Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the activities index.")

def description(request, activity_name):
    return HttpResponse("This is the description page for {}".format(activity_name))
