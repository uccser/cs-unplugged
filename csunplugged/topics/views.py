from django.shortcuts import get_object_or_404, render

from .models import Topic

def index(request):
    all_topics = Topic.objects.order_by('name')
    context = {
        'all_topics': all_topics
    }
    return render(request, 'topics/index.html', context)

def topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'topics/topic.html', {'topic': topic})
