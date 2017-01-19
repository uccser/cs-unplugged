from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.template import loader

def index(request):
    # return HttpResponse('Hello, world!')
    # template = loader.get_template('what-should-this-be-called/index.html')
    template = loader.get_template('index.html')
    # return render(request, template)
    return HttpResponse(template.render({}, request))

def example(request):
    template = loader.get_template('example.html')
    return HttpResponse(template.render({}, request))

def lesson_one_how_binary_digits_work(request):
    template = loader.get_template('lesson-one-how-binary-digits-work.html')
    return HttpResponse(template.render({}, request))

