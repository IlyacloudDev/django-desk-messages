from django_filters import FilterSet

from .models import Announcement, Comment


class AnnouncementsFilter(FilterSet):
    class Meta:
        model = Announcement
        fields = {
            'title': ['icontains'],
        }


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = [
            'announcement'
        ]

    def __init__(self, *args, **kwargs):
        super(CommentFilter, self).__init__(*args, **kwargs)
        self.filters['announcement'].queryset = Announcement.objects.filter(author__author_name=kwargs['request'])
