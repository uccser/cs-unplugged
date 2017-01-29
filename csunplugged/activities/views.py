from django.http import HttpResponse
from django.shortcuts import render
from .models import Activity

def index(request):
    all_activities = Activity.objects.order_by('name')
    context = {
        'all_activities': all_activities
    }
    return render(request, 'activities/index.html', context)

def description(request, activity_name):
    return HttpResponse("This is the description page for {}".format(activity_name))
