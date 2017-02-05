from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import generic

from .models import Topic, FollowUpActivity

class IndexView(generic.ListView):
    template_name = 'topics/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')


class TopicView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic.html'
    slug_url_kwarg = 'topic_slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TopicView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected follow up activities
        context['follow_up_activities'] = FollowUpActivity.objects.filter(topic=self.object).order_by('name')
        return context


class ActivityList(generic.ListView):
    model = FollowUpActivity
    template_name = 'topics/activity_list.html'
    context_object_name = 'all_follow_up_activities'

    def get_queryset(self, **kwargs):
        """Return all activities for topic"""
        # TODO: Is this the best way to raise 404 if invalid topic?
        topic = get_object_or_404(Topic, name=self.kwargs.get('topic_slug', None))
        return FollowUpActivity.objects.filter(topic__name=self.kwargs.get('topic_slug', None)).order_by('name')


class ActivityView(generic.DetailView):
    model = FollowUpActivity
    queryset = FollowUpActivity.objects.all()
    template_name = 'topics/activity.html'
    context_object_name = 'activity'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model,
            topic__name=self.kwargs.get('topic_slug', None),
            name=self.kwargs.get('activity_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ActivityView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected follow up activities
        context['activity_curriculum_links'] = self.object.curriculum_links.all()
        return context
