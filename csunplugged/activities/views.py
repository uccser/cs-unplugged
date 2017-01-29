from django.shortcuts import get_object_or_404, render
from .models import Activity

def index(request):
    all_activities = Activity.objects.order_by('name')
    context = {
        'all_activities': all_activities
    }
    return render(request, 'activities/index.html', context)

def activity(request, activity_slug):
    activity = get_object_or_404(Activity, slug=activity_slug)
    return render(request, 'activities/activity.html', {'activity': activity})
